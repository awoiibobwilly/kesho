from django.contrib import admin
from .models import * #we are trying to access our models upon which we are going to buils interfaces from admin panel/dashboard 
#alternatively we could say 
#from .models import stayperiod, keep

# Register your models here.
admin.site.register(Categorystay)
admin.site.register(Attendee)
admin.site.register(Payment)


