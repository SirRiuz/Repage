

# Django
from django.contrib import admin
from .settings import ( MEDIA_ROOT,MEDIA_URL )
from django.urls import path
from django.conf.urls.static import static


from accounts.client.views import AuthViewManager
from .client.views import HomeManager
from pages.client.views import CreatePage,JoinPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',AuthViewManager.as_view()),
    path('home/' , HomeManager.as_view()),
    path('page/',CreatePage.as_view()),
    path('page/<pagename>/' , JoinPage.as_view())
] + static(MEDIA_URL,document_root=MEDIA_ROOT)


