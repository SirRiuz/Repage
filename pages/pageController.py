
# Django
from django.http import HttpResponse
from core.settings import BASE_DIR
from django.template import loader
from django.shortcuts import (render,redirect)


# Python
import os
import mimetypes
#import magic ---> Eliminar libreria


# Utils
from .adsController import Ads



class PageController(object):

    def __getNotFountError(self,request) -> (HttpResponse):
        path = str(request.get_full_path())
        host_name = str(request.get_host()).split('.')[0]
        error_file = str(BASE_DIR)+'/media/'+'404.html'


        if os.path.exists(error_file):
            return HttpResponse(
                open(error_file,'rb'),
                content_type='text/html'
            )

        if path == '/':
            return render(request , 'empy_project.html')

        return render(request,'not_found_page.html',context=({
            'route':path,
            'host_name':host_name,
        }),status=404)


    def __isNotFountPage(self,path) -> (bool):
        if '/404.html' == path:
            return True
        return False
    

    def getPageByNamespace(self,request,namespace) -> (HttpResponse):
        browser_path = str(request.get_full_path())
        if not self.__isNotFountPage(browser_path):
            file_path = str(BASE_DIR)+'/media/'+namespace+'/'+browser_path.replace('/','/')     # Corregir esto ...
            type_file = ''

            if browser_path is '/':
                file_path = file_path+'index.html'

            
            type_file = mimetypes.guess_type(file_path)[0]
        
            if os.path.exists(file_path) and not os.path.isdir(file_path):
                
                file = open(file_path,'rb')

                if type_file == 'text/html':

                    loaderTemplate = loader.render_to_string(
                        file_path,{
                        'user':'Locked object ...',
                        'request':'Locked object ...',
                        'csrf_input':'Locked object ...',
                        'csrf_token':'Locked object ...'
                        },
                        request
                    )

                    requestObject = HttpResponse(loaderTemplate,content_type=type_file)
                    htmlAppendAds = Ads(requestObject.content).insertAds()
                    return HttpResponse(htmlAppendAds)
                    #return render(request,file_path,)
                
                return HttpResponse(file,content_type=type_file)
            return self.__getNotFountError(request)

        return redirect('/')

