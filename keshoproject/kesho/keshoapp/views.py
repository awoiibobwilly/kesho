from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'keshoapp/index.html')
@login_required
def about (request):
    return render(request, 'keshoapp/about.html')
def home(request):
    return render(request, 'keshoapp/home.html')
def attendant(request):
    return render(request, 'keshoapp/attendant.html')
#def attendee(request):
    return render(request, 'keshoapp/attendee.html')

#Trying to add attendee form
def AddAttendee(request):
    #addedAttendee = attendee.objects.get(id=pk)
    getattendeeform = AddAttendeeForm()
    AttendeeForm = AddAttendeeForm(request.POST)
    if request.method == 'POST':
        if AttendeeForm.is_valid():
            AttendeeForm.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'keshoapp/attendee.html', {'getattendeeform': getattendeeform,})
    #attendeeform = addattendees(request.POST)
    #if request.method == 'POST':
        #if attendeeform.is_valid():
            #newattendee = attendeeform.save(commit=False)
            #newattendee.save
    #return render(request, 'keshoapp/attendees.html', {'attendeesform': attendeesForm})
def AddPayment(request):
    #addedAttendee = attendee.objects.get(id=pk)
    getpaymentform = AddPaymentForm()
    return render(request, 'keshoapp/payment.html', {'getpaymentform': getpaymentform,})
            
    