from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render_to_response, render
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django_twilio.decorators import twilio_view

from .forms import EmergencyContactForm
from .models import EmergencyContact, Home, Alert
from .serializers import AlertSerializer
from .notification import sendEmail, sendTextMessage


def search_for_home(nickname):
    try:
        return Home.objects.get(nickname=nickname)
    except:
        return False


def create_emergency_contact(request):
    if request.method == "POST":
        form = EmergencyContactForm(request.POST)
        if form.is_valid():
            user = request.user
            home_name = form.cleaned_data['home_name']
            print request.body, type(request.body)
            if not search_for_home(home_name):
                # response = HttpResponseRedirect(settings.SETTINGS_PATH + '/html/create_emergency_contact.html')
                # response.write("<p>Unrecognized Home Name! Please try again</p>")
                return render(
                    request,
                    settings.SETTINGS_PATH + '/html/error_create_emergency_contact.html',
                    {'emergency_contact_form': form}
                )
            print User.objects.get(id=user.id)
            print home_name
            # print form, type(form)
            EmergencyContact.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email'],
                home=Home.objects.get(nickname=home_name)
            )
            # redirect, or however you want to get to the main view
            return HttpResponseRedirect(settings.SETTINGS_PATH + '/html/main.html')
    else:
        form = EmergencyContactForm()

    return render(
        request,
        settings.SETTINGS_PATH + '/html/create_emergency_contact.html',
        {'emergency_contact_form': form}
    )

@twilio_view
def send_alert(request):
    if request.method == 'GET':
        sendTextMessage('4163718808', 'lolcats make me hungry')
    elif request.method == 'POST':
        try:
            print 'BODY'
            print request.body
        except:
            pass
        try:
            print 'DATA'
            print request.data
        except:
            pass

        data = {
            'result': True,
            'note': 'Looks like this worked yay!'
        }

    return Response({'True': 'SUCCESS'}, status=status.HTTP_200_OK)


class AlertView(APIView):
    """
    User goals view set
    """
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = (AllowAny,)
    model = Alert

    def get(self, request):
        # user = request.user
        # if not isinstance(user, User):
        #     return Response({'error': 'not User instance'}, status=status.HTTP_401_UNAUTHORIZED)

        sendTextMessage('4163718808', 'lolcats make me hungry')
        # sendEmail("kailon.f@gmail.com", "Hello", "Your House Is On Fire")
        return Response({'True': 'Sent Notification!'}, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            print 'HEADER'
            print request.header
        except:
            pass
        try:
            print 'QUERY PARAMS'
            print request.query_params
        except:
            pass
        try:
            print 'BODY'
            print request.body
        except:
            pass
        try:
            print 'DATA'
            print request.data
        except:
            pass
        try:
            print 'CONTENT TYPE'
            print request.content_type
        except:
            pass
        try:
            print 'STREAM'
            print request.stream
        except:
            pass
        return Response({'True': 'SUCCESS'}, status=status.HTTP_200_OK)

