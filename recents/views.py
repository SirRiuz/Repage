
# rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response


# Models
from pages.models import Page
from .models import RecentItem


# Serializers


class RecentsManager(APIView):

    """
    
      Se encarga de administrar los archivos recientes.
      Los archivos recientes son una pequeña caracteristica
      que desidi añadir estos consisten en un pequeño historial
      que muestran los 4 primeros archivos que el usiario a abierto 
      a largo del dia

    """

    def get(self,request,page=None) -> (Response):
        """
          Obtiene todos los archivos recientes
        """

        if not page is None: 
            pageObject = Page.objects.filter(name=page)
            recentObject = None
            userObject = request.user

            if len(pageObject) > 0:
                pageObject = pageObject[0]
                recentObject = RecentItem.objects.filter(page=pageObject)

                print(recentObject)
                return Response(page)
            
            else:
                return Response({
                    'status':'error',
                    'type-error':'page-error',
                    'messege':'The page not exits ...'
                },status=200)

        else:
            return Response({ 'status':'error' },status=400)


    def post(self,request,page=None) -> (Response):
        return Response({})

