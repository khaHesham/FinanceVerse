from flask_wtf import FlaskForm
from werkzeug.exceptions import Locked
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FloatField, DateField 
from wtforms import validators
from wtforms.fields.choices import SelectField
from wtforms.validators import Length, EqualTo, DataRequired,NumberRange


class SignUp_Form(FlaskForm): 
    username=StringField(label='Username',validators=[Length(min=2,max=30), DataRequired()])
    name=StringField(label='Name',validators=[Length(min=2,max=60),DataRequired()])
    password1= PasswordField(label='password1',validators=[Length(min=8),DataRequired()])
    bank_acc=IntegerField(label='Bank Account',validators=[DataRequired(),NumberRange(min=0,message="please insert only positive numbers")])
    address=StringField(label='Address',validators=[Length(min=2),DataRequired()])
    phone=StringField(label='Phone',validators=[Length(min=11,max=11),DataRequired()])
    signup= SubmitField(label='sign up')


class LogIn_Form(FlaskForm):
    usernamee=StringField(label='Username',validators=[Length(min=2,max=30),DataRequired()])
    passwordd= PasswordField(label='password1',validators=[Length(min=8),DataRequired()])
    login=SubmitField(label='login')


class Admin_numbers(FlaskForm):
    cust_num=IntegerField()
    payments_num=IntegerField()
    Loans_num=IntegerField()
    Transctions_num=IntegerField()
    cust_username=StringField()
    cust_balance=IntegerField()
    cust_username=StringField()
    Data=dict()

class Profile_Form(FlaskForm):
    Username=StringField(label='Username')
    Name = StringField(label='Name')
    Address = StringField(label='Address')
    Phone = StringField(label='phone')


class Credit_Form(FlaskForm):
    Credit_Balance = FloatField(label="Balance")
    Credit_ID = StringField(label = "Credit_ID")
    acc_id = IntegerField(label="acc_id")

class Bank_Form(FlaskForm):
    Acc_Balance = FloatField(label="Balance")
    Bank_id = IntegerField(label="bank_id")
    Bank_Name = StringField(label="Name")

class Add_Asset_Form(FlaskForm):
    Add = SubmitField(label="Add")
    Cost = FloatField(label="Cost", validators=[DataRequired(),NumberRange(min=0,message="please insert only positive numbers")])
    Type = SelectField(label="Choose a Type", choices=['Choose a Type', 'Home', 'Company', 'Car'], validators=[DataRequired()])

class Delete_Asset_Form(FlaskForm):
    delete = SubmitField(label="Delete")
    cst = FloatField(label="Cost", validators=[DataRequired(),NumberRange(min=0,message="please insert only positive numbers")])
    typ = SelectField(label="Choose a Type", choices=['Choose a Type', 'Home', 'Company', 'Car'], validators=[DataRequired()])
   
class usernames(FlaskForm):
    users=SelectField(label='Users',validators=[DataRequired()])
    make=SubmitField(label="Make",validators=[DataRequired()])

class password_Updater(FlaskForm):
    password=PasswordField(label='password',validators=[Length(min=8),DataRequired()])
    check_pass=PasswordField(label='check password',validators=[Length(min=8),DataRequired()])
    submit=SubmitField(label="change")

class Payment_Form(FlaskForm):
    Value = FloatField(label='Value', validators=[DataRequired()])
    destination_id = IntegerField(label="destination_id", validators=[DataRequired(),NumberRange(min=0,message="please insert only positive numbers")])
    Pay = SubmitField(label = "Pay", validators=[DataRequired()])

class Loan_Form(FlaskForm):
    Amount = IntegerField(label='Amount', validators=[DataRequired(),NumberRange(min=0,message="please insert only positive numbers")])
    Type = SelectField(label="Choose a Type", choices=['Choose a Type', 'Payday', 'Short term', 'Long term'], validators=[DataRequired()])
    Request_Loan = SubmitField(label = "Request A Loan", validators=[DataRequired()])



class Transaction_Form(FlaskForm):
    Amnt = IntegerField(label= "Amount", validators=[DataRequired(),NumberRange(min=0,message="please insert only positive numbers")])
    stock_id = SelectField(label="Choose a Stock", validators=[DataRequired()])
    Invest = SubmitField(label = "Invest", validators=[DataRequired()])