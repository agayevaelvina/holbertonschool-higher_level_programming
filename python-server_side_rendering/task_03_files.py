from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Example product data (you can load from JSON file if needed)
products = [
    {"id": 1, "name": "Laptop", "price": 999},
    {"id": 2, "name": "Coffee Mug", "price": 12},
    {"id": 3, "name": "Smartphone", "price": 599}
]

@app.route('/products')
def products_route():
    source = request.args.get('source', 'json')
    id_str = request.args.get('id')

    if source != 'json':
        return "Wrong source", 400

    if id_str:
        try:
            prod_id = int(id_str)
        except ValueError:
            return "Invalid ID", 400

        product = next((p for p in products if p['id'] == prod_id), None)
        if not product:
            return "Product not found", 404
        # Return product JSON as string (or render template)
        return jsonify(product)

    # Return all products as JSON list
    return jsonify(products)

if __name__ == "__main__":
    # Use use_reloader=False to avoid double startup in background run
    app.run(debug=True, use_reloader=False)
