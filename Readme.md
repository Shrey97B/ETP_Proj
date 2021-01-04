# Equity Trading Portfolio

This is a Tkinter based desktop application. Tkinter is a python based GUI framework for creating desktop applications with some basic but effective widgets available. The application developed here is the Equity Trading Portfolio, which is a platform for stock market trading system using which a user may place orders for buying or selling shares of the company. The project was created for academic purpose, and so the functionalities and methodologies implemented were to adhere to the provided problem definition.
The project mainly focuses on creating a GUI and database based application with help of tkinter. Procedures and jobs have also been used in database for handling orders. An attempt has also been made to create maintainable code and follow design principles like implementing singleton pattern in DB connection and separating the necessary concerns by using OOP constructs and principles in python.

The platform supports and works by collaboration of three kinds of users: Traders, Brokers and Adminstrator.

## Trader Module:

Trader is the user who has ownership over stocks and wants to trade them over the stock exchange. 
* Registration; A Trader must first register in order to use the system.
* Login: In order to access the functionalities the user has to login to the system.
* View Account Information: Trader can view his/her information entered in the system.
* Portfolio: Using this module, a user may view various stocks owned by him/her and its details.
* Buy Order: Buying a stock is a three step process. A trader will initially place a request for buying an order to a broker. Any order request will last only for five minutes (will be expired on exceeding duration) otherwise user may end up paying unexpected price. After the order is accepted by the broker, trader will click on buy and make payment. Payments are done in the system using a dummy wallet associated with each Trader. Various constraints have been looked after, before executing the order. If payment becomes successful, amount is deducted and stocks are transferred to the portfolio of Trader.
* Sell Order: Selling a stock is only two step process. A trader will place the request for selling the stock under his/her ownership. The request goes to Broker who on successful selling the stocks will lead the prices of shares to be transferred to trader’s account. Here, also the order has to be completed within 5 minutes, otherwise it will get expired.
* Order Details: A trader may view order history, pending or expired orders and recently accepted orders placed by him/her.
* View Stock Information: A Trader may also view the Information of Stocks in the System. It displays a graph with necessary details of the stocks over past few days.

## Broker Module:
The Broker type user is associated with actual trading of stocks from order requests of Traders and performing necessary procedures at stock exchange to facilitate the Trader from virtually anywhere.
* Registration; A Broker must first register in order to use the system.
* Login: In order to access the functionalities the user has to login to the system.
* View Account Information: Broker can view his/her information entered in the system.
* Update Brokerage: A broker can update the brokerage into system using this functionality so that the next upcoming orders follow the updated brokerage.
* Stock Information: A Trader may also view the Information of Stocks in the System. It displays a graph with necessary details of the stocks over past few days.
* Accept Buy Orders: A broker can accept the orders placed for him/her by any Trader so that the broker can buy the stocks from marketplace and transfer them over to Trader.
* Accept Sell Orders: Similar to Buy orders, a broker can also accept sell orders so stocks will be sold back to marketplace and amount of share will be transferred in Trader’s account.
* Order History: A broker can view the details of all the orders that he/she is associated with.

## Administrator Module:
Admin is the central authority and will add the new stock into database so that system can work with newly added stocks and can also view stock information.

Refer to the **Screenshots** directory to view screenshots of the project.

## Running Project

Since this is a python based projects, one will need he following libraries for implementing the project.
* cx_oracle
* nsetools (to get live price during order transaction)
* nsepy (for history of share price)
* configParser
* tkinter

The database used by the project was of Oracle and the project had been tested using both Oracle 11g and later with 18c databases. However, one might need client libraries like InstaClient provided by Oracle. Use queries and PLSQL scripts in the DBschema directory to setup your database tables, sequences, procedures. Also, it is required to add an admin user through database query.

The username, password and url for database should be configured in the dbconfig.ini file.

After setting up the database and code, execute the project by running the file `Sampa.py`.
