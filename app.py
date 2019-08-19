import nexmo
import africastalking

class smsService:
	def nexmoClient(sms):

	def atClient(sms):

	def smsServiceProcessor(sms,provider):
		if(provider == 'Nexmo'):
			nexmoClient(sms)
		elif(provider == 'AfricasTalking')
			atClient(sms)
		else:
			return "Invalid provider"


if __name__ == '__main__':
    app.run(debug=True)
