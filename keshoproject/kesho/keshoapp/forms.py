from django.forms import ModelForm
from .models import *

#Below here, we are creating a model
class AddAttendeeForm(ModelForm):
    class Meta:
        model = Attendee
        fields = '__all__' 
class AddPaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__' 
