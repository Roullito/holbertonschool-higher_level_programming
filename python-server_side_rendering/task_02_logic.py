from flask import Flask, render_template
import json

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)
