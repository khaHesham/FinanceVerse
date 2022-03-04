create database FINANCEVERSE;
use FINANCEVERSE;

create table USER
(
Username varchar(30),
Password varchar(200) NOT NULL,

primary key(Username)
);

create table CUSTOMER
(
Customer_ID int AUTO_INCREMENT,
Name varchar(30) NOT NULL,
Address varchar(30),
Phone varchar(14),
Is_Admin int,

username varchar(30) NOT NULL,

primary key(Customer_ID),
foreign key(username) references USER(Username)
);

create table COMPANY
(
Company_ID int AUTO_INCREMENT,
Name varchar (30) NOT NULL,
Address varchar(30),

primary key (Company_ID)
);


create table BANK
(
Bank_ID int,
Name varchar(20) NOT NULL,
Loc varchar(20) NOT NULL,

primary key (Bank_ID)
);


create Table BANK_ACCOUNT
(
Acc_ID int,
Balance float,

bank_id int NOT NULL,
username varchar(30),

primary key (Acc_ID),
foreign key(username) references USER(Username),
foreign key(bank_id) references BANK(Bank_ID)
);


create table PAYMENT
(
Payment_ID int AUTO_INCREMENT,
Date date NOT NULL,
Value float NOT NULL,
source_id int NOT NULL,
destination_id int NOT NULL,

primary key(Payment_ID),
foreign key(source_id) references BANK_ACCOUNT(Acc_ID),
foreign key(destination_id) references BANK_ACCOUNT(Acc_ID)
);


create table LOAN
(
Loan_ID int AUTO_INCREMENT,
Type varchar (20) NOT NULL,
Date date NOT NULL,
Amount int NOT NULL,

acc_id int NOT NULL,

primary key(Loan_ID),
foreign key(acc_id) references BANK_ACCOUNT(Acc_ID)
);

create table CREDIT_CARD
(
Credit_ID varchar(16),
Balance float,

acc_id int NOT NULL,

primary key(Credit_ID),
foreign key(acc_id) references BANK_ACCOUNT(Acc_ID)
);


create table STOCK
(
Stock_ID int AUTO_INCREMENT,
Count int NOT NULL,
Name varchar(20) NOT NULL,
Price float NOT NULL,

company_id int NOT NULL,

primary key(Stock_ID),
foreign key(company_id) references COMPANY(Company_ID)
);
 

create table TRANSACTION
(
Trans_ID int AUTO_INCREMENT,
Date date NOT NULL,
Amount float NOT NULL,

stock_id int NOT NULL,
customer_id int NOT NULL,

primary key(Trans_ID),
foreign key(stock_id) references STOCK(Stock_ID),
foreign key(customer_id) references CUSTOMER(Customer_ID)
);


create table ASSET
(
Type varchar(10), 
Cost float,

customer_id int NOT NULL,

primary key (customer_id, Type, Cost),
foreign key(customer_id) references CUSTOMER(Customer_ID)
);


create table GUARANTEE
(
loan_id int NOT NULL, 
customer_id int NOT NULL, 
cost float NOT NULL,
type varchar (10),

primary key(customer_id, type, cost, loan_id),
foreign key(loan_id) references LOAN(Loan_ID),
foreign key (customer_id, type, cost) references ASSET(Customer_ID, Type, Cost)
);