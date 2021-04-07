
# Django
from django.urls import path



# Views
from .views import RecentsManager

urlpatterns = [
    path('recents/',RecentsManager.as_view()),
    path('recents/<page>/',RecentsManager.as_view())
]
