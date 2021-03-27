

# Django
from django.urls import (path,include)


urlpatterns = [
    path('v1/',include('pages.api.urls')),
    path('v1/',include('accounts.urls')),
]



