import os
import smtplib

#Cell carriers list to append to the end of a phone number

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

#Which address the email gets sent from

senderaddress = {
	'notifications':    'notifications@customwebsite.com',
	'accounts': 'accounts@customwebsite.com',
    'support':    'support@customwebsite.com',
	'bugreport': 'bugreport@customwebsite.com',
    'information': 'information@customwebsite.com',
}

#Sends the message to the phone number

def send(message, phonenumber, carrier, fromaddress):
    to_number = str(phonenumber) + str(carriers[carrier])
    fromaddress = senderaddress[fromaddress]
    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(str(fromaddress), str(to_number), str(message))         
        print("Successfully sent email")
    except SMTPException:
        print("Error: unable to send email")

