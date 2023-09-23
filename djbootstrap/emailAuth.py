from django.shortcuts import render
from sites.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.core.mail import EmailMessage

MESSAGE = """
    Hello {username}, 
    please authenticate your email by clicking the fallowing link:
    {url}
"""

def authenticate_email(request, site, guid, user):
    url = request.build_absolute_uri(site + "/" + guid)
    send_mail("authenticate email", MESSAGE.format(username=user.username, url=url), EMAIL_HOST_USER, [user.email], fail_silently=False,)
    return render(request, "verifyEmail.html")