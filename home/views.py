
from xml.dom import ValidationErr
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.urls import reverse
from .forms import ContactForm
from .models import Contacts
from django.utils.timezone import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
   
    if request.POST:

        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        title = request.POST.get('title')
        message = request.POST.get('message')

        if len(fullname) == "" or len(fullname) <3 or len(title)<3:
            messages.error(request, "please fill the form correclty")
                           

        else:
            db_contact = Contacts()
            db_contact.fullname = fullname
            db_contact.email = email
            db_contact.title = title
            db_contact.message = message
            db_contact.date = datetime.date(datetime.today())
            db_contact.save()
            messages.success(request, "Message sent successfully")
            return redirect(request.path)

    if request.GET:
        return render(request, "home.html")

    return render(request, "home.html")


    