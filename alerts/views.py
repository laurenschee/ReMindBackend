from django.shortcuts import render
from django.http import HttpResponse
from .utils import send_twilio_message
from django_twilio.decorators import twilio_view

# Create your views here.


@twilio_view
def send_alert(request):
    if request.method == 'GET':
        send_twilio_message('4163718808', 'lolcats make me hungry')
    elif request.method == 'POST':
        print request.body
        # phone_number = request.data['phone_number']
        # message = request.data['message']
        send_twilio_message('6475270741', 'Hi Michael your house is on fire')

    return HttpResponse("sent message")