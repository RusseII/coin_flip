from send_sms import sendText

class Engine():
	def __init__(self):
		print "creating engine object"

	def run(self):
		send=sendText()
		send.send_text()


