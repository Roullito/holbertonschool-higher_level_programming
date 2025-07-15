from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def items():
    filename = "items.json"
    with  open(filename, "r") as f:
        data = json.load(f)
    items_list = data["items"]
    return render_template("items.html", items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
