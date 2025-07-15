from flask import Flask, render_template, request
import json
import csv

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
        filename = "items.json"
        with  open(filename, "r") as f:
            data = json.load(f)
        items_list = data["items"]
        return render_template("items.html", items=items_list)
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return render_template("items.html", items=[])

@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    error = None
    products = []

    if source == "json":
        try:
            with open("products.json", "r") as f:
                data = json.load(f)
            products = data
        except Exception:
            error = "Could not read JSON file."

    elif source == "csv":
        try:
            with open("products.csv", "r") as f:
                reader = csv.DictReader(f)
                products = []
                for row in reader:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    products.append(row)
        except Exception:
            error = "Could not read CSV file."

    else:
        error = "Wrong source"
        return render_template("product_display.html", error=error)

    if id_param and not error:
        try:
            search_id = int(id_param)
            filtered = [p for p in products if int(p['id']) == search_id]
            if filtered:
                products = filtered
            else:
                error = "Product not found"
                products = []
        except Exception:
            error = "Invalid id"
            products = []

    return render_template("product_display.html", products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
