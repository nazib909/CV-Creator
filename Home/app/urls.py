from django.urls import path
from .views import *
 
urlpatterns = [
    path('', cv, name='cv'),
    path('forgot/', forgot, name='forgot'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('createProf/', createProf, name='createProf')
]