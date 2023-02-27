from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', cv, name='cv'),
    path('forgot/', forgot, name='forgot'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('createProf/', createProf, name='createProf'),
    path('createCV/', createCV, name='createCV'),
    path('setting/', setting, name='setting'),
    path('logout/', logout, name='logout'),
    path('delete/<id>/', delete, name='delete'),
    path('password/',changePassword, name='changePassword')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
