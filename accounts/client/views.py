

from django.shortcuts import render
from django.views import View


class AuthViewManager(View):

    def get(self,request) -> (render):
        return render(request,'auth/login.html')





