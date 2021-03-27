

# Django
from django.urls import (path,re_path)

# Views
from .page import pageApiManager
from .file import FileApiManager
from .uploads import FileUploadManager


urlpatterns = [
    re_path(r'^file/',FileApiManager.as_view()),
    path('page/',pageApiManager.as_view()),
    path('upload/',FileUploadManager.as_view()),
    path('page/<str:pageName>/',pageApiManager.as_view())
]
