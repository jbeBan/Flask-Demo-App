from flask import Flask, url_for, render_template
import re


app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")

@app.route("/summary")
def summary():
  orders = None
  with open("order_report.txt", 'r') as f:
    orders = f.read()
    orders = orders.split("===========================")[1:]

  return render_template("summary.html", orders=orders)

@app.route("/dates")
def dates():
  dates = None
  with open("order_report.txt", 'r') as f:
    dates = f.read()
    dates = re.findall(r'Order #[\d]+, Date: [\d]+-[\d]+-[\d]+', dates)

  return render_template("dates.html", dates=dates)

@app.route("/payments")
def payments():
  return render_template("payments.html")

@app.route("/customers")
def customers():
  return render_template("customers.html")
