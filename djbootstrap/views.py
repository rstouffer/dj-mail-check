from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from djbootstrap.forms import SignupForm, LoginForm, SetUsername, SetPassword
from djbootstrap.models import GUID, ExtraInfo
from djbootstrap.emailAuth import authenticate_email
import uuid, time

from djbootstrap.viewsAuth import *

def index(request): 
    if request.user.is_authenticated:
        return HttpResponseRedirect("/welcome")

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/welcome")
    else:
        form = LoginForm()

    return render(request, "index.html", {"form": form})

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data["username"], form.cleaned_data["email"], form.cleaned_data["password"])
            user.save()

            extraData = ExtraInfo(
                user = user,
                first_name = form.cleaned_data["first_name"],
                last_name = form.cleaned_data["last_name"],

                company_name = form.cleaned_data["company_name"],

                address_l1 = form.cleaned_data["address_l1"],
                address_l2 = form.cleaned_data["address_l2"],

                city = form.cleaned_data["city"],
                state = form.cleaned_data["state"],
                zip_code = form.cleaned_data["zip_code"],

                phone = form.cleaned_data["phone"]
            )
            extraData.save()

            guid = GUID(user=user, guid=uuid.uuid4().hex, time=time.time())
            guid.save()

            return authenticate_email(request, "signup", guid.guid, user)
    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})

def verify_page(request, id):
    guid = GUID.objects.get(guid=id)
    login(request, guid.user, backend='django.contrib.auth.backends.ModelBackend')

    if (time.time() - guid.time <= 3600):
        guid.delete()

    return HttpResponseRedirect("/welcome")

def forgot_my_password_start(request):
    if (request.method == "POST"):
        form = SetUsername(request.POST)

        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data["username"])

            forgot = GUID(guid=uuid.uuid4().hex, user=user, time = time.time())
            forgot.save()
            
            return authenticate_email(request, "forgotpassword", forgot.guid, user)
    else:
        form = SetUsername()
        
    return render(request, "getEmail.html", {"form": form})
    
def forgot_my_password_end(request, id):
    if (request.method == "POST"):
        form = SetPassword(request.POST)
        if form.is_valid():
            forgot = GUID.objects.get(guid=id)
            login(request, forgot.user, backend='django.contrib.auth.backends.ModelBackend')
            if (time.time() - forgot.time <= 3600):
                forgot.user.set_password(form.cleaned_data["password"])
                forgot.user.save()
                forgot.delete()
            
            return HttpResponseRedirect("/welcome")
    else:
        form = SetPassword()
        
    return render(request, "getPassword.html", {"id": id, "form": form})