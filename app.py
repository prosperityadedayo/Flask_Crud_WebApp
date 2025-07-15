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

@app.route('/add', methods=['POST'])
def add_utensil():
    if request.method == "POST":
        Item_name = request.form['Item_name']
        Material = request.form['Material']
        Quantity = request.form['Quantity']
        Sale = request.form['Sale']
        Purchase = request.form['Purchase']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO kitchen_utensils (Item_name, Material, Quantity, Sale, Purchase) VALUES (%s, %s, %s, %s, %s)", (Item_name, Material, Quantity, Sale, Purchase))

        mysql.connection.commit()
        return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
