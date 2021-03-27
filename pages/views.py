

# Django
from django.http.response import HttpResponse
from django.views import View

# Models
from .models import Page


# Controllers
from .pageController import PageController


class pageViewManager(View):

    def get(self,request) -> (HttpResponse):
        name_page = str(request.get_host()).split('.')[0]
        page_object = Page.objects.filter(name=name_page)
        if page_object:
            page_object = page_object[0]
            if page_object.isAcces:
                page_controller_object = PageController()
                request_object = page_controller_object.getPageByNamespace(
                    request,
                    page_object.namespace
                )

                return request_object
            
            return HttpResponse('Esta pagina ya no esta disponible ...')

        return HttpResponse('Page not found ...')








