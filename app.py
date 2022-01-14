from flask import Flask, url_for, render_template
from datetime import date
from json import load
import re


app = Flask(__name__)

with open("market_orders.json", 'r') as data:
  market_orders = load(data)["market_orders"]


@app.route("/")
def index():
  return render_template("index.html")

@app.route("/summary")
def summary():
  return render_template("summary.html", orders=market_orders)

@app.route("/dates")
def dates():
  orders_by_date = sorted(market_orders, key=lambda x: date(int(x["date"].split("/")[2]), int(x["date"].split("/")[0]), int(x["date"].split("/")[1])))
  
  return render_template("dates.html", orders_by_date=orders_by_date)

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
