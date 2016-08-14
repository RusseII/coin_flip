from flask import Flask, render_template
from engine.engine import Engine
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template("index.html")
	


@app.route("/text")
def text():
	return Engine().run()


if __name__ == "__main__":
    app.run(debug=True)