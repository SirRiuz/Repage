

# rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# Serializers
from .serializers import (PageSerializerClass,PageSerializer)


# Models
from ..models import Page



class pageApiManager(APIView):
    """
      Esta clase tiene los metodos
      que permiten obtemer , crear
      y eliminar paginas
    """

# Authorization: Token 839b05426935df97cc631b927ac4f70729bee4cd

    permission_classes = [ IsAuthenticated ]

    def __isOwner(self,user,queryObject) ->(bool):
        if queryObject.user == user:
            return True

        return False

    def get(self,request,pageName='default') -> (Response):
        """
          Obtiene una pagina por su 
          nombre
        """
        query = None

        if pageName != 'default':
            if (not pageName is None):
                query = Page.objects.filter(name=pageName)
                if len(query) > 0:
                    query = query[0]
                    serializer = PageSerializerClass(query,many=False)
                    return Response({
                        'statis':'ok',
                        'isOwner':self.__isOwner(request.user,query),
                        'data':serializer.data
                    },status=status.HTTP_200_OK)
                else:
                    return Response(({
                        'status':'error',
                        'type-error':'page-nox-found',
                        'messege':'The page not exits ...'
                    }),
                    status=status.HTTP_404_NOT_FOUND
                )
            else:
                query = Page.objects.all()
                serializer = PageSerializerClass(query,many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)

        else:
            query = Page.objects.filter(user=request.user)
            pageList = PageSerializerClass(query,many=True)
            return Response({
                'status':'ok',
                'pages':pageList.data
            })


    def post(self,request,pageName=None) -> (Response):
        """
          Permite crear una pagina
        """
        user = request.user
        serializer = PageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        responseData = serializer.create(
            model=Page,
            data=serializer.data,
            user=user
        )
        return Response(responseData)
    

    def delete(self,request,pageName=None) -> (Response):
        print(pageName)
        serializer = PageSerializer()
        data = serializer.delete(pageName,Page)
        return Response(data)

    
