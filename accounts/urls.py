

# Django
from django.urls import  path


# Views
from .views import (AuthManager,RegisterManager)



urlpatterns = [
    path('auth/',AuthManager.as_view()),
    path('register/<mode>/',RegisterManager.as_view())
]



