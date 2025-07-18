from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        return []

def read_csv(file_path):
    products = []
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert price to float and id to int
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except Exception as e:
        return []

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error = None

    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')
    else:
        error = "Wrong source"
        return render_template("product_display.html", error=error)

    # Convert dict keys to dot notation using SimpleNamespace
    from types import SimpleNamespace
    products = [SimpleNamespace(**p) for p in products]

    if product_id:
        filtered = [p for p in products if p.id == product_id]
        if not filtered:
            error = "Product not found"
        else:
            products = filtered

    return render_template("product_display.html", products=products, error=error)
