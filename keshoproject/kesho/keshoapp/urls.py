from django.urls import path
from keshoapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('home/', views.home, name = 'home'),
    path('attendant/', views.attendant, name = 'attendant'),
    path('attendee/', views.AddAttendee, name = 'AddAttendee'),
    path('payment/', views.AddPayment, name = 'AddPayment'),
    path('login/', auth_views.LoginView.as_view(template_name='keshoapp/login.html'),name ='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='keshoapp/logout.html'),name ='logout'),
    
]