from django.urls import path
from ecommerceapp import views


urlpatterns = [
    
    path('',views.index,name="index"),
    path('contacr',views.contact,name="contact"),
]



