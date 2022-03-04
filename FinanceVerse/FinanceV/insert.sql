INSERT INTO BANK VALUES(1, 'CIB', 'cairo');
INSERT INTO BANK_ACCOUNT VALUES(1, 1000000, 1, null), (2, 1000, 1, null);
INSERT INTO CREDIT_CARD VALUES(1010, 20000, 1), (2020, 1000, 2);

INSERT INTO COMPANY VALUES (1, 'Apple', 'USA'), (2, 'Netflix', 'USA');
INSERT INTO STOCK(Count, Name, Price, company_id) VALUES(1000, 'AAPL', 300, 1), (500, 'NFLX', 200, 2);



INSERT INTO COMPANY VALUES (3, 'Facebook', 'USA');
INSERT INTO COMPANY VALUES (4, 'Google', 'USA');
INSERT INTO COMPANY VALUES (5, 'Tesla', 'USA');
INSERT INTO COMPANY VALUES (6, 'Amazon', 'Egypt');
INSERT INTO COMPANY VALUES (7, 'Khaled_AI', 'october');
INSERT INTO COMPANY VALUES (8, 'dabdob', 'haram');

INSERT INTO STOCK(Count, Name, Price, company_id) VALUES(600, 'FBK', 350, 1);
INSERT INTO STOCK(Count, Name, Price, company_id) VALUES(300, 'GGL', 200, 2);
INSERT INTO STOCK(Count, Name, Price, company_id) VALUES(100, 'TSLA', 500, 1);
INSERT INTO STOCK(Count, Name, Price, company_id) VALUES(500, 'AMZN', 900, 2);
INSERT INTO STOCK(Count, Name, Price, company_id) VALUES(1000, 'AI', 400, 1);
INSERT INTO STOCK(Count, Name, Price, company_id) VALUES(50, 'DBDB', 150, 2);