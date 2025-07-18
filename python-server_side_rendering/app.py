from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def get_data_from_json():
    return [
        {'id': 1, 'name': 'Laptop', 'price': 799.99, 'category': 'Electronics'},
        {'id': 2, 'name': 'Coffee Mug', 'price': 15.99, 'category': 'Home Goods'}
    ]

def get_data_from_csv():
    data = []
    try:
        with open('products.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'price': float(row['price']),
                    'category': row['category']
                })
    except Exception as e:
        data = []
    return data

def get_data_from_sql():
    data = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, price, category FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            data.append({
                'id': row[0],
                'name': row[1],
                'price': row[2],
                'category': row[3]
            })
        conn.close()
    except sqlite3.Error as e:
        data = None  # Signal error
    return data

@app.route('/products')
def products():
    source = request.args.get('source')

    if source == 'json':
        products = get_data_from_json()
    elif source == 'csv':
        products = get_data_from_csv()
    elif source == 'sql':
        products = get_data_from_sql()
        if products is None:
            return render_template('product_display.html', error='Database error.')
    else:
        return render_template('product_display.html', error='Wrong source.')

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
