from flask import Flask, url_for, render_template
from tinydb import TinyDB, Query
import re


app = Flask(__name__)
db = TinyDB("market_orders.json")


@app.route("/")
def index():
  print(db)
  return render_template("index.html")

@app.route("/summary")
def summary():
  orders = None
  with open("data_summary.txt", 'r') as f:
    orders = f.read()
    orders = orders.split("===========================")[1:]

  return render_template("summary.html", orders=orders)

@app.route("/dates")
def dates():
  dates = None
  with open("data_summary.txt", 'r') as f:
    dates = f.read()
    dates = re.findall(r'Order #[\d]+, Date: [\d]+-[\d]+-[\d]+', dates)

  return render_template("dates.html", dates=dates)

@app.route("/payments")
def payments():
  payments = None
  with open("data_summary.txt", 'r') as f:
    payments = f.read()
    payments = re.findall(r'Amount: \$[\d]+\.[\d]+, Paid by .+', payments)

  return render_template("payments.html", payments=payments)

@app.route("/customers")
def customers():
  customers = None
  with open("data_summary.txt", 'r') as f:
    customers = f.read()
    customers = re.findall(r'Customer ID #[0-9]{6}:\n.+\n.+\n[a-zA-Z ]+, [A-Z]{2} [0-9]{5}', customers)

  return render_template("customers.html", customers=customers)
