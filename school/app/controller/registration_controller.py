from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse

def index(request):
    msg = ''
    if request.method == 'POST':  # POST, we get all fields from registration page
        req = request.POST.dict()
        username = req['username']
        password = req['password']
        email = req['email']  # this is our target email
        try:  # we try to find existing user first, if exists show error
            user = User.objects.get(username=username)
            msg = 'Username or E-Mail is already registered'
        except User.DoesNotExist:  # user not found, then register, send email
            user = User.objects.create_user(username, email, password)  # register user
            user.save()  # save to db
            msg = ''  # empty message, no error, then send mail using configured EMAIL_HOST_USER
            send_mail(
                'Registration Successful',
                'You are now a database administrator of SMA Negeri 1 Indonesia!',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=True,
            )
        return HttpResponseRedirect(reverse('login'))  # show login page if successful
    data = {
        'user_exists_error': msg,
    }
    return render(request, 'registration/registration.html', data)