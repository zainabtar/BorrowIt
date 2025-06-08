To run this project on your machine:

1. Install dependencies:
pip install flask mysql-connector-python

2. Set up the MySQL database:
Create a database named: borrowit_db
Import the table creation SQL

3. Update app.py with your DB login:
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password=,
    database='borrowit_db')
   
4.Run the application:
app.py

5.Open the browser:
Go to the provided link
The homepage should display all items
You can navigate to /add and /register manually
