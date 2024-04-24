from django.db import models
from django.utils import timezone

# Create your models here.
class Categorystay(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.name

    
class Attendee(models.Model):
    c_stay = models.ForeignKey(Categorystay,on_delete=models.CASCADE, null = True, blank = True)
    a_name = models.CharField(max_length=200,null=True, blank=True)
    age = models.IntegerField(null=True, blank=True, default=0)
    gender = models.CharField(max_length=10,null=True, blank=True)
    location = models.CharField(max_length=50,null=True, blank=True)
    bringer = models.CharField(max_length=200,null=True, blank = True)
    timein = models.DateTimeField(null=True, blank=True, default=0)
    timeout = models.DateTimeField(null=True, blank=True, default=0)
    
    def __str__(self):
        return self.a_name
    
class Payment(models.Model):
    b_fee = models.ForeignKey(Attendee,on_delete=models.CASCADE, null = True, blank = True)
    c_payment = models.ForeignKey(Categorystay,on_delete=models.CASCADE, null = True, blank = True)
    payamount = models.IntegerField(null=True, blank=True)
    paynum = models.IntegerField(null=True, blank=True)
    paycurrency = models.CharField(max_length= 10, default= 'UGX', null= True, blank=True)
    
def __int__(self):
    return self.paynum   
    

    

    
