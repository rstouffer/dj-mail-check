import time
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from djbootstrap.forms import ChangeInfo, SetEmail
from djbootstrap.models import GUID
from djbootstrap.emailAuth import authenticate_email
import uuid

def welcome(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")
    
    user = request.user

    try:
        GUID.objects.get(user=user)
        warning = True
    except GUID.DoesNotExist:
        warning = False

    return render(request, "welcome.html", {"username": user.username, "email": user.email, "warning": warning})

def changeInfo(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")
    
    try:
        GUID.objects.get(user=request.user)
        return HttpResponseRedirect("/welcome")
    except GUID.DoesNotExist:
        pass

    user = request.user
    
    if request.method == "POST":
        form = ChangeInfo(request.POST)

        if form.is_valid() and authenticate(username=user.username, password=form.cleaned_data["prevPassword"]) == user:
            if form.cleaned_data["username"] != "":
                user.username = form.cleaned_data["username"]
            if form.cleaned_data["email"] != "":
                user.email = form.cleaned_data["email"]
            if form.cleaned_data["newPassword"] != "":
                user.set_password(form.cleaned_data["newPassword"])

            if form.cleaned_data["first_name"] != "":
                user.first_name = form.cleaned_data["first_name"]
            if form.cleaned_data["last_name"] != "":
                user.last_name = form.cleaned_data["last_name"]
            if form.cleaned_data["company_name"] != "":
                user.company_name = form.cleaned_data["company_name"]
            if form.cleaned_data["address_l1"] != "":
                user.address_l1 = form.cleaned_data["address_l1"]
            if form.cleaned_data["address_l2"] != "":
                user.address_l2 = form.cleaned_data["address_l2"]
            if form.cleaned_data["city"] != "":
                user.city = form.cleaned_data["city"]
            if form.cleaned_data["state"] != "":
                user.state = form.cleaned_data["state"]
            if form.cleaned_data["zip_code"] != "":
                user.zip_code = form.cleaned_data["zip_code"]
            if form.cleaned_data["phone"] != "":
                user.phone = form.cleaned_data["phone"]
            user.save()

            guid = GUID(user=user, guid=uuid.uuid4().hex, time=time.time())
            guid.save()

            return authenticate_email(request, "changeinfo", guid.guid, user)
    else:
        form = ChangeInfo()

    return render(request, "changeInfo.html", {"form": form})

def logout_page(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")
    
    logout(request)
    return HttpResponseRedirect("/")

def setEmail_start(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")
    
    if (request.method == "POST"):
        form = SetEmail(request.POST)

        if form.is_valid():
            request.user.email = form.cleaned_data['email']
            request.user.save()

            if form.is_valid():
                try:
                    GUID.objects.get(user=request.user).delete()
                except GUID.DoesNotExist:
                    pass

                forgot = GUID(guid=uuid.uuid4().hex, user=request.user, time = time.time())
                forgot.save()
                
                return authenticate_email(request, "setemail", forgot.guid, request.user)
    else:
        form = SetEmail()
    
    return render(request, "getEmail2.html", {"form": form})

def setEmail_end(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")
    
    guid = GUID.objects.get(guid=id)

    if (time.time() - guid.time <= 3600):
        guid.delete()
    
    return HttpResponseRedirect("/welcome")

def delete_account(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")
    
    if request.method == "POST":
        request.user.delete()
        return HttpResponseRedirect("/")
    
    return render(request, "deleteAccount.html")


__all__ = ["welcome", "changeInfo", "logout_page", "delete_account", "setEmail_start", "setEmail_end"]