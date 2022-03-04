from FinanceV import ExecuteQuery, app, SelectQuery, SelectMultipleQuery
from functools import wraps
from flask import render_template,redirect,url_for, session, flash
from FinanceV.forms import Profile_Form, SignUp_Form, LogIn_Form, Admin_numbers, Add_Asset_Form, Credit_Form, Bank_Form, Payment_Form, Loan_Form, Transaction_Form, Delete_Asset_Form, password_Updater, usernames
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from datetime import date
from werkzeug.security import check_password_hash, generate_password_hash


def login_required(f):
    """Decorate routes to require login."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("Username") is None:
            return redirect("/Signin")
        return f(*args, **kwargs)
    return decorated_function
#=================================================ROUTES===========================================================

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/Signin',methods=['GET','POST'])
def register_page():
    form2=SignUp_Form()
    form=LogIn_Form()

    if form2.validate_on_submit():
        res = SelectMultipleQuery("SELECT Acc_ID FROM BANK_ACCOUNT where username is NULL;")
        valid_ids = [it['Acc_ID'] for it in res]
        exist_username = SelectQuery(f'''SELECT Username FROM user WHERE Username='{form2.username.data}';''')
        if not exist_username:
            if(form2.bank_acc.data in valid_ids):
                password_hashed = generate_password_hash(form2.password1.data)
                ExecuteQuery(f'''INSERT INTO user(Password,Username) VALUES ('{password_hashed}','{form2.username.data}');''')
                ExecuteQuery(f'''INSERT INTO customer(Name,address,phone, Is_Admin, username) VALUES ('{form2.name.data}','{form2.address.data}','{form2.phone.data}', 0, '{form2.username.data}');''')
                ExecuteQuery(f'''UPDATE BANK_ACCOUNT SET username = '{form2.username.data}' WHERE Acc_ID = {form2.bank_acc.data};''') 
                return redirect(url_for('register_page'))
            else:
                flash("Enter a valid account ID",'alert')
                redirect(url_for('register_page'))
        else:
            flash("Username already exists",'alert')
            redirect(url_for('register_page'))

    if form.validate_on_submit():
        valid_username = SelectQuery(f'''SELECT Username FROM user WHERE Username='{form.usernamee.data}'; ''')

        if (valid_username):
            user_password = SelectQuery(f"SELECT Password FROM user WHERE Username='{form.usernamee.data}';")['Password']
            correct_password = check_password_hash(user_password, form.passwordd.data)
            if(correct_password):
                # Forget any user_id
                session.clear()
                # Remember which user has logged in
                session["Username"] = form.usernamee.data
                return redirect(url_for('profile'))
            else:
                flash("Incorrect Password",'alert')
        else:
            flash("Incorrect Username",'alert')

    return render_template('SignIn.html',form=form,form2=form2)

@app.route('/Profile',methods=['GET','POST'])
@login_required
def profile():
    Profile_form = Profile_Form()
    credit_form= Credit_Form()
    bank_form = Bank_Form()
    Add_Asset = Add_Asset_Form()
    Delete_Asset= Delete_Asset_Form()
    update_pass=password_Updater()

    Username = session['Username']
    Profile_form.Username.data = Username

    customer = SelectQuery(f"SELECT Is_Admin, customer_id, Name, Address, Phone FROM CUSTOMER WHERE Username = '{Username}';")
    customer_id = customer['customer_id']
    Profile_form.Name.data = customer['Name']
    Profile_form.Address.data = customer['Address']
    Profile_form.Phone.data = customer['Phone']
    is_admin = customer['Is_Admin']




    credit_card = SelectQuery(f"SELECT CREDIT_CARD.Balance, Credit_ID, CREDIT_CARD.acc_id FROM CREDIT_CARD, BANK_ACCOUNT WHERE username = '{Username}' AND CREDIT_CARD.acc_id= BANK_ACCOUNT.Acc_id;")
    if credit_card:
        credit_form.Credit_Balance.data = credit_card['Balance']
        credit_form.Credit_ID.data = credit_card['Credit_ID']
        credit_form.acc_id.data = credit_card['acc_id']
    
    bank = SelectQuery(f"SELECT Balance, BANK.bank_id, Name FROM BANK_ACCOUNT, BANK WHERE Username = '{Username}' AND BANK_ACCOUNT.bank_id=BANK.Bank_ID;")    
    bank_form.Acc_Balance.data = bank['Balance']
    bank_form.Bank_id.data = bank['bank_id']
    bank_form.Bank_Name.data = bank['Name']

    assets = SelectMultipleQuery(f"SELECT Type, Cost FROM ASSET WHERE customer_id =  {customer_id} ;")    

    #=================================================================================================================================================================================================
    if Add_Asset.validate_on_submit():
        exist = SelectQuery(f"SELECT * FROM ASSET WHERE Type = '{Add_Asset.Type.data}' AND Cost = {Add_Asset.Cost.data} AND customer_id = {customer_id};")
        if(not exist):
            ExecuteQuery(f"INSERT INTO ASSET VALUES ('{Add_Asset.Type.data}', {Add_Asset.Cost.data}, {customer_id});")
            flash('Updated Successfully!', 'success')
        else:
            flash('Cannot Update!', 'alert')

    if Delete_Asset.validate_on_submit():
        donee = ExecuteQuery(f'''Delete from asset where Cost={Delete_Asset.cst.data} AND Type='{Delete_Asset.typ.data}' AND customer_id={customer_id};''')    
        if (donee):
            flash('Deleted Successfully!', 'success')
        else:
            flash('Cannot Delete!', 'alert')


    if update_pass.validate_on_submit():
        password_hashed = generate_password_hash(update_pass.password.data)
        update=ExecuteQuery(f'''update user set Password='{password_hashed}' where Username='{Username}';''')
        if (update):
            flash('Changed Successfully!', 'success')
        else:
            flash('Cannot change!', 'alert')

    return render_template('Profile.html', Profile_form = Profile_form, credit_form = credit_form, Add_Asset=Add_Asset, assets=assets, bank_form=bank_form, Delete_Asset=Delete_Asset, update_pass=update_pass, is_admin = is_admin)

@app.route('/Actions',methods=['GET','POST'])
@login_required
def Actions():
    payment_form = Payment_Form()
    loan_form = Loan_Form()
    transaction_form = Transaction_Form()
    username = session['Username']
    Date = date.today()

    customer_id = SelectQuery(f"SELECT customer_id FROM CUSTOMER WHERE Username = '{username}';")['customer_id']
    source_id = SelectQuery(f"SELECT Acc_ID FROM BANK_ACCOUNT WHERE username = '{username}';")['Acc_ID']
    stocks = SelectMultipleQuery("SELECT Name, Stock_ID FROM STOCK;")
    transaction_form.stock_id.choices = [(stock['Stock_ID'], stock['Name']) for stock in stocks]
    transaction_form.stock_id.choices.insert(0, (0, 'Choose a Stock'))

    #============================================================================================================================================================================
    if payment_form.validate_on_submit():
        balance = SelectQuery(f"SELECT Balance FROM BANK_ACCOUNT WHERE username = '{username}';")['Balance']
        new_balance = balance - payment_form.Value.data
        enough_balance = new_balance >= 0

        res = SelectMultipleQuery("SELECT Acc_ID FROM BANK_ACCOUNT;")
        valid_ids = [it['Acc_ID'] for it in res]
        valid_ids.remove(source_id)

        valid = payment_form.destination_id.data in valid_ids

        if(not enough_balance):
            flash("Not enough Balance", "alert")
            return redirect(url_for("Actions"))
        if(not valid):
            flash("Enter a valid destination ID", "alert")
            return redirect(url_for("Actions"))


        exists = SelectQuery(f"SELECT * FROM PAYMENT WHERE Date = '{Date}' AND Value = {payment_form.Value.data} AND source_id = {source_id} AND destination_id = {payment_form.destination_id.data};")
        if not exists:
            ExecuteQuery(f"INSERT INTO PAYMENT(Date, Value, source_id, destination_id) VALUES ('{Date}', {payment_form.Value.data}, {source_id}, {payment_form.destination_id.data});")
            ExecuteQuery(f"UPDATE BANK_ACCOUNT SET Balance = {new_balance} WHERE username = '{username}';")
            ExecuteQuery(f"UPDATE BANK_ACCOUNT SET Balance = Balance + {payment_form.Value.data} WHERE acc_id = {payment_form.destination_id.data};")
            flash("Payment Done", "success")
        else:
            flash("Payment already done", "alert")
    #==================================================================================================================================================================================
    if loan_form.validate_on_submit():
        exists = SelectQuery(f"SELECT * FROM LOAN WHERE Type = '{loan_form.Type.data}' AND Date = '{Date}' AND Amount = {loan_form.Amount.data} AND acc_id = {source_id};")
        if not exists:
            ExecuteQuery(f"INSERT INTO LOAN (Type, Date, Amount, acc_id) VALUES ('{loan_form.Type.data}', '{Date}', {loan_form.Amount.data}, {source_id});")
            flash("Loan Requested Successfully!", "success")
        else:
            flash("Loan already requested", "alert")   

    #==================================================================================================================================================================================
    if transaction_form.validate_on_submit():
        stock_info  = SelectQuery(f"SELECT Count, Price FROM STOCK WHERE Stock_ID = {transaction_form.stock_id.data};")
        if not stock_info:
            flash("Please choose a stock", "alert")
            return redirect(url_for("Actions"))
        new_count = stock_info['Count'] - transaction_form.Amnt.data
        
        balance = SelectQuery(f"SELECT Balance FROM BANK_ACCOUNT WHERE username = '{username}';")['Balance']

        To_pay = stock_info['Price'] * transaction_form.Amnt.data
        new_balance = balance - To_pay

        enough_shares = new_count >= 0
        enough_balance = new_balance >= 0

        if(not enough_shares):
            flash("Not enough shares", "alert")
            return redirect(url_for("Actions"))
        if(not enough_balance):
            flash("Not enough Balance", "alert")
            return redirect(url_for("Actions"))
        
        exists = SelectQuery(f"SELECT * FROM TRANSACTION WHERE Date = '{Date}' AND Amount = {transaction_form.Amnt.data} AND stock_id = {transaction_form.stock_id.data} AND customer_id = {customer_id};")
        if not exists:
            ExecuteQuery(f"INSERT INTO TRANSACTION(Date, Amount, stock_id, customer_id) VALUES('{Date}', {transaction_form.Amnt.data}, {transaction_form.stock_id.data}, {customer_id});")
            ExecuteQuery(f"UPDATE BANK_ACCOUNT SET Balance = {new_balance} WHERE username = '{username}';")
            ExecuteQuery(f"UPDATE STOCK SET Count = {new_count} WHERE Stock_ID = {transaction_form.stock_id.data};")
            flash("Transaction Done", "success")
        else:
            flash("Transaction already done", "alert")   
    #========================================================================================================================================================================================

    return render_template('Actions.html', payment_form=payment_form, loan_form=loan_form, transaction_form=transaction_form)

@app.route('/trans_History')
@login_required
def trans_history():
    form=Admin_numbers()
    Username = session['Username']
    form.cust_username.data=Username
    ID=SelectMultipleQuery(f'''SELECT Customer_ID FROM customer where username='{Username}';''')[0]['Customer_ID']
    Acc_ID=SelectMultipleQuery(f'''SELECT Acc_ID FROM bank_account where username='{Username}';''')[0]['Acc_ID']
    form.payments_num.data=SelectMultipleQuery(f'''SELECT COUNT(*) FROM payment where source_id={Acc_ID} or destination_id={Acc_ID};''')[0]['COUNT(*)']
    form.Loans_num.data=SelectMultipleQuery(f'''SELECT COUNT(*) FROM loan where acc_id={Acc_ID};''')[0]['COUNT(*)']
    form.Transctions_num.data=SelectMultipleQuery(f'''SELECT COUNT(*) FROM Transaction where customer_id={ID};''')[0]['COUNT(*)']
    data=SelectMultipleQuery(f'''SELECT stock.Name as stockName ,transaction.amount,
    transaction.Date from transaction,stock where transaction.customer_ID={ID}
     AND transaction.stock_ID=stock.Stock_ID;''')
    return render_template('TransactionsHistory.html',form=form,data=data)

@app.route('/loans_History')
@login_required
def loans_history():
    form=Admin_numbers()
    Username = session['Username']
    form.cust_username.data=Username
    ID=SelectMultipleQuery(f'''SELECT Customer_ID FROM customer where username='{Username}';''')[0]['Customer_ID']
    Acc_ID=SelectMultipleQuery(f'''SELECT Acc_ID FROM bank_account where username='{Username}';''')[0]['Acc_ID']
    form.payments_num.data=SelectMultipleQuery(f'''SELECT COUNT(*) FROM payment where source_id={Acc_ID} or destination_id={Acc_ID};''')[0]['COUNT(*)']
    form.Loans_num.data=SelectMultipleQuery(f'''SELECT COUNT(*) FROM loan where acc_id={Acc_ID};''')[0]['COUNT(*)']
    form.Transctions_num.data=SelectMultipleQuery(f'''SELECT COUNT(*) FROM Transaction where customer_id={ID};''')[0]['COUNT(*)']
    data=SelectMultipleQuery(f'''SELECT loan.Amount,loan.Type,loan.Date from loan
     where loan.acc_id={Acc_ID} ''')
    return render_template('LoansHistory.html',form=form,data=data)

@app.route('/payments_History')
@login_required
def payments_history():
    form=Admin_numbers()
    Username = session['Username']
    form.cust_username.data=Username
    ID=SelectMultipleQuery(f'''SELECT Customer_ID FROM customer where username='{Username}';''')[0]['Customer_ID']
    Acc_ID=SelectMultipleQuery(f'''SELECT Acc_ID FROM bank_account where username='{Username}';''')[0]['Acc_ID']
    form.payments_num.data=SelectMultipleQuery(f'''SELECT COUNT(*) FROM payment where source_id={Acc_ID} or destination_id={Acc_ID} ;''')[0]['COUNT(*)']
    form.Loans_num.data=SelectMultipleQuery(f'''SELECT COUNT(*) FROM loan where acc_id={Acc_ID};''')[0]['COUNT(*)']
    form.Transctions_num.data=SelectMultipleQuery(f'''SELECT COUNT(*) FROM Transaction where customer_id={ID};''')[0]['COUNT(*)']
    data=SelectMultipleQuery(f'''SELECT R.username,payment.value, Date
      from bank_account as R,payment where payment.source_id= {Acc_ID} AND R.Acc_ID=payment.destination_id;''')
    data2=SelectMultipleQuery(f'''SELECT S.username ,payment.value, Date
      from bank_account as S,payment where payment.destination_id={Acc_ID} AND S.Acc_ID=payment.source_id;''')  
    return render_template('PaymentsHistory.html',form=form,data=data,data2=data2)

@app.route('/Admin_actions',methods=['GET','POST'])
def Admin_actions():
    Users=usernames()
    datas=SelectMultipleQuery('''select Username from customer where Is_Admin=0;''')
    Users.users.choices = [data['Username'] for data in datas]
    Users.users.choices.insert(0, 'Choose a Username')
    
    if Users.validate_on_submit():
        make=ExecuteQuery(f'''update customer set Is_Admin=1 where Username='{Users.users.data}';''')
        if (make):
            flash('Changed Successfully!', 'success')
        else:
            flash('Cannot change!', 'alert')

    return render_template('AdminActions.html',Users=Users)

@app.route('/admin')
@login_required
def Admin():
    """too"""
    form=Admin_numbers()
    form.cust_num.data=SelectMultipleQuery('''SELECT COUNT(*) FROM customer;''')[0]['COUNT(*)']
    form.payments_num.data=SelectMultipleQuery('''SELECT COUNT(*) FROM payment;''')[0]['COUNT(*)']
    form.Loans_num.data=SelectMultipleQuery('''SELECT COUNT(*) FROM loan;''')[0]['COUNT(*)']
    form.Transctions_num.data=SelectMultipleQuery('''SELECT COUNT(*) FROM Transaction;''')[0]['COUNT(*)']
    data=SelectMultipleQuery('''SELECT distinct bank_account.Username, Address, Phone,Balance from user,customer,bank_account where bank_account.Username=user.Username AND customer.Username=user.Username  ;''')
    data3=SelectMultipleQuery('''Select distinct Name,count,price from stock;''')
    data2=[data['Name'] for data in data3]  
    data4=[data['count'] for data in data3]
    data5=[data['price'] for data in data3]
    return render_template("AdminPage.html",form=form,data=data,data2=data2,data4=data4, data5=data5)

@app.route('/AdminTrans')
@login_required
def Admin_Trans():
    form=Admin_numbers()
    form.cust_num.data=SelectMultipleQuery('''SELECT COUNT(*) FROM customer;''')[0]['COUNT(*)']
    form.payments_num.data=SelectMultipleQuery('''SELECT COUNT(*) FROM payment;''')[0]['COUNT(*)']
    form.Loans_num.data=SelectMultipleQuery('''SELECT COUNT(*) FROM loan;''')[0]['COUNT(*)']
    form.Transctions_num.data=SelectMultipleQuery('''SELECT COUNT(*) FROM Transaction;''')[0]['COUNT(*)']
    data=SelectMultipleQuery('''SELECT customer.username,stock.Name as stockName ,transaction.amount,
    Date from customer,transaction,stock 
    where transaction.customer_ID=customer.Customer_ID
     AND transaction.stock_ID=stock.Stock_ID;''')
    return render_template("AdminTransactions.html",form=form,data=data)

@app.route('/AdminLoans')
@login_required
def Admin_Loans():
    form=Admin_numbers()
    form.cust_num.data=SelectMultipleQuery('''SELECT COUNT(*) FROM customer;''')[0]['COUNT(*)']
    form.payments_num.data=SelectMultipleQuery('''SELECT COUNT(*) FROM payment;''')[0]['COUNT(*)']
    form.Loans_num.data=SelectMultipleQuery('''SELECT COUNT(*) FROM loan;''')[0]['COUNT(*)']
    form.Transctions_num.data=SelectMultipleQuery('''SELECT COUNT(*) FROM Transaction;''')[0]['COUNT(*)']
    data=SelectMultipleQuery('''SELECT L.username,loan.Amount,loan.Type,loan.Date from bank_account as L,loan
     where loan.acc_id=L.Acc_ID ;''')
    return render_template("AdminLoans.html",form=form,data=data)   

@app.route('/Adminpayments')
@login_required
def Admin_Payments():
    form=Admin_numbers()
    form.cust_num.data=SelectMultipleQuery('''SELECT COUNT(*) FROM customer;''')[0]['COUNT(*)']
    form.payments_num.data=SelectMultipleQuery('''SELECT COUNT(*) FROM payment;''')[0]['COUNT(*)']
    form.Loans_num.data=SelectMultipleQuery('''SELECT COUNT(*) FROM loan;''')[0]['COUNT(*)']
    form.Transctions_num.data=SelectMultipleQuery('''SELECT COUNT(*) FROM Transaction;''')[0]['COUNT(*)']
    data=SelectMultipleQuery('''SELECT S.username as sender,R.username as reciever,payment.value, Date
      from bank_account as S,bank_account as R,payment where S.Acc_ID=payment.source_id 
      AND R.Acc_ID=payment.destination_id;''')
    return render_template("AdminPayments.html",form=form,data=data)

@app.route("/Logout")
def logout():
    session.clear()

    return redirect("/")

#==================================================================================================================

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return f"{e.name}, {e.code}"

# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
