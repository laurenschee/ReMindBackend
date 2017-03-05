from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
from sendsms.message import SmsMessage
import smtplib
import os

# Need a more secure way to store passwords
BASE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE, "pw.txt")) as f:
    passwords = f.readlines()
# Remove the new line character
account_id = str(passwords[0]).strip('\n')
auth_token = str(passwords[1]).strip('\n')
email_password = str(passwords[2])


def sendTextMessage(recipient, msg):
    """
    Sends a text message

    param recipient: phone number of the recipient
    param msg: text message to be sent to the recipient

    type recipient: string
    type msg: string

    return: none
    rtype: None
    """

    # message = SmsMessage(body=msg, from_phone='+12267770962', to=[recipient])
    # message.send()
    try:
        print account_id, type(account_id)
        print auth_token, type(auth_token)
        print 'RECIPIENT', recipient
        print 'MESSAGE', msg
        client = TwilioRestClient(account_id, auth_token)
        client.messages.create(to=recipient, from_="+12267770962", body=msg)
    except TwilioRestException as e:
        print e

def sendEmail(email_recipient, subject, msg):
    """
    Sends a email

    param email_recipient: email of the recipient
    param sub:
    param msg: text message to be sent to the recipient

    param email_recipient: email of the recipient
    param sub:
    param msg: text message to be sent to the recipient

    return: none
    rtype: None
    """

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('alertremind@gmail.com', email_password)
    smtpObj.sendmail('alertremind@gmail.com', email_recipient, 'Subject:'+ subject +'\n' + msg)
    smtpObj.quit()

# sendTextMessage("6475270741", "yo does this work?")
# sendEmail("michaelwyshin@gmail.com", "Hello", "This test works")
