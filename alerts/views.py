from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .utils import send_twilio_message
from django_twilio.decorators import twilio_view
from reMind.models import Home, Sensor, EmergencyContact
from reMind.notification import sendEmail

# Create your views here.


@twilio_view
def send_alert(request):
    if request.method == 'POST':
        print request.body
        parameter_list = [p.split('=') for p in request.body.split('&')]
        parameters = dict(parameter_list)
        try:
            sensor = Sensor.objects.get(arduino_id=parameters['UUID'])
            # print "SENSOR"
            user = sensor.owner
            # print "got USEr"
            sensor_name = sensor.nickname
            # print "got SENSOR NICKNAME"
            contact = EmergencyContact.objects.filter(owner=user).first()
            # print "got EMERGENCY CONTACT"
            phone = contact.phone
            # print "got PHONE"
            first_name = contact.first_name
            # print "got FIRST NAME"
            home_name = sensor.home.nickname
            # print "got HOME NAME"
            message = make_message(first_name, sensor_name, home_name, parameters)
            send_twilio_message(phone, message)
            # print "SENT MESSAGE"
        except:
            pass
        return HttpResponse("sent message")

    return HttpResponseBadRequest("POST request expected. Please try again")


def send_email_alert(request):
    if request.method == 'POST':
        print request.body
        parameter_list = [p.split('=') for p in request.body.split('&')]
        parameters = dict(parameter_list)
        try:
            sensor = Sensor.objects.get(arduino_id=parameters['UUID'])
            user = sensor.owner
            sensor_name = sensor.nickname
            contact = EmergencyContact.objects.filter(owner=user).first()
            email = contact.email
            first_name = contact.first_name
            home_name = sensor.home.nickname
            message = make_message(first_name, sensor_name, home_name, parameters)
            sendEmail(email, "ReMind Alert!", message)
        except:
            pass
        return HttpResponse("sent email")

    return HttpResponseBadRequest("POST request expected. Please try again")


def make_message(first_name, sensor_name, home_name, parameters):
    if parameters['above']:
        above_below = 'above'
    else:
        above_below = 'below'
    message = 'Hi '+first_name+\
              ', this is an alert from '+sensor_name+\
              ' in '+home_name+\
              '. It has measured a '+parameters['measurement']+\
              ' at '+parameters['value']+\
              ' centimeters for '+parameters['duration']+\
              ' minutes, which is '+above_below+' where it should be.'
    return message