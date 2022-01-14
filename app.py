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
  return render_template("payments.html", orders=market_orders)

@app.route("/users")
def users():
  users = [{"username": x["username"], "full_name": x["full_name"]} for x in market_orders]

  return render_template("users.html", users=users)
