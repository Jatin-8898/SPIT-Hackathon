from app import app

from flask import render_template

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/stock")
def index():
	return render_template("stock.html")


if __name__ == "__main__":
	app.run(host="localhost",port=8000,debug=True)

