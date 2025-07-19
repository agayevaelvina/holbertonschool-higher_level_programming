#!/usr/bin/env python3
#
from flask import Flask, render_template,request
import json
import csv
import sqlite3


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open("items.json","r") as f:
            baza= json.load(f)
            items=baza.get("items",[])
    except Exception:
        items=[]
    return render_template("items.html", items=items)


def json_file_read():
    try:
        with open("products.json","r") as f_json:
            return json.load(f_json)
    except Exception:
        return []

def csv_file_read():
    try:
        with open("products.csv",newline="") as f_csv:
            read=csv.DictReader(f_csv)
            products=[]
            for row in read:
                products.append({
                    "id": int(row["id"]),
                    "name":row["name"],
                    "category":row["category"],
                    "price":float(row["price"])
                })
        return products
    except Exception:
        return[]

@app.route('/products')
def display_products():
    istochnik= request.args.get("source")
    id_param=request.args.get("id")
    products=[]
    error= None

    if istochnik =='json':
        products =json_file_read()
    elif istochnik =='csv':
        products=csv_file_read()
    elif istochnik =="sql":
        products=load_from_sqlite()
        if products is None:
            return "Database error occured", 500 
    else:
        error = "Wrong source"
        return render_template('product_display.html',products=products, error=error)

    if id_param:
        try:
            product_id=int(id_param)
            products = [p for p in products if p['id'] == product_id]
            if not products:
                error = "Product not found"
        except ValueError:
            error="Invalid ID format"
            products=[]

    return render_template('product_display.html',products=products, error=error)

def load_from_sqlite():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, category FROM Products")
        rows=cursor.fetchall()
        conn.close()
        products=[]
        for row in rows:
            products.append({
                "id":row[0],
                "name":row[1],
                "price":row[2],
                "category":row[3]
             })
        return products
    except sqlite3.Error:
        print("Error database")
        return None



if __name__ == '__main__':
    app.run(debug=True, port=5000)
