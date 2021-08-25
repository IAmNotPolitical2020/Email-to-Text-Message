from flask import Flask
from flask_mail import Mail
from flask_mail import Message

MAIL_SERVER = 'mail.customwebsite.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

carriers = {
	'att':    '@mms.att.net',
	'tmobile':' @tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@messaging.sprintpcs.com',
    'alltel':   '@sms.alltelwireless.com',
    'boost':   '@sms.myboostmobile.com',
    'cricket':   '@mms.cricketwireless.net',
    'metropcs':   '@mymetropcs.com',
    'uscellular':   '@email.uscc.net',
    'virginmobile':   '@vmobl.com',
    'republicwireless':   '@text.republicwireless.com',
}

senderadress = {
	'notifications':    'notifications@customwebsite.com',
	'accounts': 'accounts@customwebsite.com',
    'support':    'support@customwebsite.com',
	'bugreport': 'bugreport@customwebsite.com',
    'information': 'information@customwebsite.com',
}

def send(message, phonenumber, carrier, fromadress):
   to_number = str(phonenumber) + str(carriers[carrier])
   fromadress = senderadress[fromadress]
   msg = Message('', sender = str(fromadress), recipients = [to_number])
   msg.body = message
   mail.send(msg)
