from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_crud_db'

mysql = MySQL(app)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/create')
def create_page():
    return render_template('create.html')

@app.route('/add', methods=['POST'])
def add_utensil():
    if request.method == "POST":
        Item_name = request.form['Item_name']
        Material = request.form['Material']
        Quantity = request.form['Quantity']
        Sales_price = request.form['Sales_price']
        Purchase_price = request.form['Purchase_price']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO kitchen_utensils (Item_name, Material, Quantity, Sales_price, Purchase_price) VALUES (%s, %s, %s, %s, %s)", (Item_name, Material, Quantity, Sales_price, Purchase_price))

        mysql.connection.commit()
        return redirect(url_for('dashboard'))

@app.route('/inventory')
def view_inventory():
    search_query = request.args.get('search', '')

    cursor = mysql.connection.cursor()
    
    if search_query:
        query = "SELECT * FROM kitchen_utensils WHERE Item_name LIKE %s"
        cursor.execute(query, ('%' + search_query + '%',))
    else:
        query = "SELECT * FROM kitchen_utensils"
        cursor.execute(query)

    utensils = cursor.fetchall()
    return render_template('inventory.html', utensils=utensils, search_query=search_query)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
