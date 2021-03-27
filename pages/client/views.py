

from django.views import View
from django.shortcuts import render



class CreatePage(View):
    def get(sefl,request) -> (render):
        return render(request,'create.html')



class JoinPage(View):
    def get(self,request,pagename) -> (render):
        return render(request,'page_admin.html')

