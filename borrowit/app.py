from flask import Flask, render_template, request, redirect
import mysql.connector  # connecting python with mysql datbase

app = Flask(__name__)

# homepage
@app.route("/")
def home():
    # connecting to database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="borrowit123",
        database="borrowit_db"
    )
    cursor = conn.cursor()

    # this fetches items from databse
    cursor.execute("SELECT item_name, item_type, building_code, status FROM items")
    items = cursor.fetchall()

    cursor.close()
    conn.close()

    # will show items on homepage
    return render_template("index.html", items=items)


# page to add new item
@app.route("/add", methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
        item_name = request.form["item_name"]
        item_type = request.form["item_type"]
        building_code = request.form["building_code"]

        # insert new item to mysql
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="borrowit123",
            database="borrowit_db"
        )
        cursor = conn.cursor()
        sql = "INSERT INTO items (item_name, item_type, building_code, status) VALUES (%s, %s, %s, %s)"
        val = (item_name, item_type, building_code, item_type)  # Use item_type as default status

        cursor.execute(sql, val)
        conn.commit()

        cursor.close()
        conn.close()

        return "Form submitted!"

    # to show add items form
    return render_template("add_item.html")


# for update item to "Returned"
@app.route("/update", methods=["POST"])
def update_status():
    item_name = request.form["item_name"]

    # connect and update status
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="borrowit123",
        database="borrowit_db"
    )
    cursor = conn.cursor()
    sql = "UPDATE items SET status = 'Returned' WHERE item_name = %s"
    cursor.execute(sql, (item_name,))
    conn.commit()

    cursor.close()
    conn.close()

    return redirect("/")  # re-loading homepage


# registration page for new users
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        building_code = request.form["building_code"]

        # save new user to database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="borrowit123",
            database="borrowit_db"
        )
        cursor = conn.cursor()
        sql = "INSERT INTO users (name, building_code) VALUES (%s, %s)"
        val = (name, building_code)
        cursor.execute(sql, val)

        conn.commit()
        cursor.close()
        conn.close()

        return "Registration successful!"

    # show registration form 
    return render_template("register.html")


# start  the app: flask
if __name__ == "__main__":
    app.run(debug=True)


