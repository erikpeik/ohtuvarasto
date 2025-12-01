from flask import Flask, render_template, request, redirect, url_for
from varasto import Varasto


app = Flask(__name__)

# In-memory storage for warehouses (name -> Varasto instance)
warehouses = {}


def parse_float(value, default=0.0):
    try:
        return float(value)
    except ValueError:
        return default


@app.route('/')
def index():
    return render_template('index.html', warehouses=warehouses)


@app.route('/create', methods=['POST'])
def create_warehouse():
    name = request.form.get('name', '').strip()
    capacity = parse_float(request.form.get('capacity', '0'))

    if name and capacity > 0:
        warehouses[name] = Varasto(capacity)

    return redirect(url_for('index'))


@app.route('/update/<name>', methods=['POST'])
def update_warehouse(name):
    if name not in warehouses:
        return redirect(url_for('index'))

    action = request.form.get('action', '')
    amount = parse_float(request.form.get('amount', '0'))

    if amount > 0:
        if action == 'add':
            warehouses[name].lisaa_varastoon(amount)
        elif action == 'take':
            warehouses[name].ota_varastosta(amount)

    return redirect(url_for('index'))


@app.route('/delete/<name>', methods=['POST'])
def delete_warehouse(name):
    if name in warehouses:
        del warehouses[name]

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
