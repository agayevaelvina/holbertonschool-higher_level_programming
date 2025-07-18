#!/usr/bin/env python3
from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/items')
def items():
    items_file = os.path.join(os.path.dirname(__file__), 'items.json')
    try:
        with open(items_file, 'r') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []

    return render_template('items.html', items=items_list)

# Only run if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)
