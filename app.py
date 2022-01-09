from flask import Flask, url_for, render_template


app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")

@app.route("/summary")
def summary():
  return render_template("summary.html")

@app.route("/dates")
def dates():
  return render_template("dates.html")

@app.route("/payments")
def payments():
  return render_template("payments.html")

@app.route("/customers")
def customers():
  return render_template("customers.html")
