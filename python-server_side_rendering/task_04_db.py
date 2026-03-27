from flask import Flask, render_template, request
import json
import csv
import os
import sqlite3

app = Flask(__name__)

def read_json_products(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []

def read_csv_products(path):
    products = []
    try:
        with open(path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return products

def read_sql_products(path):
    products = []
    try:
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        conn.close()
    except Exception as e:
        print(f"Error reading SQLite DB: {e}")
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    prod_id = request.args.get('id', type=int)
    products = []
    error = None
    base_dir = os.path.dirname(__file__)
    if source == 'json':
        products = read_json_products(os.path.join(base_dir, 'products.json'))
    elif source == 'csv':
        products = read_csv_products(os.path.join(base_dir, 'products.csv'))
    elif source == 'sql':
        products = read_sql_products(os.path.join(base_dir, 'products.db'))
    else:
        error = 'Wrong source'
        return render_template('product_display.html', error=error)

    if prod_id is not None:
        filtered = [p for p in products if int(p['id']) == prod_id]
        if not filtered:
            error = 'Product not found'
            return render_template('product_display.html', error=error)
        products = filtered

    class Product:
        def __init__(self, d):
            self.__dict__ = d
    products = [Product(p) for p in products]

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
