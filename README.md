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
    password='yourpassword',
    database='borrowit_db')
   
4.Run the application:
python app.py

5.Open the browser:
Go to http://127.0.0.1:5000/
The homepage should display all items
You can navigate to /add and /register manually
