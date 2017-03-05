from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.conf import settings

from .forms import UserForm


def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            # redirect, or however you want to get to the main view
            return HttpResponseRedirect(settings.SETTINGS_PATH + '/html/main.html')
    else:
        form = UserForm()

    return render(request, settings.SETTINGS_PATH + '/html/create_user.html', {'create_user_form': form})




        # return get_template("create_userer.html")
    # return render_to_response(settings.SETTINGS_PATH + '/html/create_user.html')
    # return HttpResponse("Hello, world. You're at the polls index.")