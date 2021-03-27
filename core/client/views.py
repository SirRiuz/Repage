

from django.views import View
from django.shortcuts import render



class HomeManager(View):


    def get(self,request) -> (render):
        return render(request,'home.html')



