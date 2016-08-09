from flask import Flask
from send_sms import sendText
app = Flask(__name__)

@app.route("/")
def hello():
	obj=sendText()
	return obj.send_text()

if __name__ == "__main__":
    app.run()