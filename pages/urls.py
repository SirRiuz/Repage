
# Django
from django.urls import (path,re_path)


# Views
from .views import pageViewManager


urlpatterns = [
    re_path(r'^',pageViewManager.as_view()),
]



