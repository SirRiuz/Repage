
# python 
import os
import random

# rets_framework
from rest_framework.response import Response
from rest_framework.views import APIView
from core.settings import BASE_DIR,MEDIA_DIR
from rest_framework import status


from ..utils import (fileData,pathRecursiveFile)


# Serializers
from .serializers import (FileSerializer,UpdateFileSerializer)


# Models
from ..models import Page


class FileApiManager(APIView):

    def __getFilePath(self,fullPath) -> (str):
        path = str(fullPath)
        path = path.replace('/v1/file/','')
        path = path.split('?')
        path = path[0]
        path = path.replace('/','\\')
        return path

    def __getPageObjectModel(self,pageName) -> (object):
        query = Page.objects.filter(name=pageName)
        if len(query) >= 1:
            query = query[0]
            return query

        return None


    def get(self,request) -> (Response):
        pageName = request.GET.get('page','')
        path = self.__getFilePath(request.get_full_path())
        query = Page.objects.filter(name=pageName)

        if len(query) > 0:
            query = query[0]
            absolutePath = MEDIA_DIR+query.namespace+'\\'+path.replace('%20',' ')
            print('path -> '+path.replace('%20',' '))

            if os.path.exists(absolutePath):
                if os.path.isdir(absolutePath):
                    return Response({
                        'status':'ok',
                        'path':path,
                        'thread':pathRecursiveFile(absolutePath)
                    },status=status.HTTP_200_OK)
                else:
                    try:
                        return Response({
                            'status':'ok',
                            'path':path,
                            'namespace':query.namespace,
                            'data':fileData(absolutePath)
                        },status=status.HTTP_200_OK)
                    except Exception:
                        return Response({
                            'status':'error',
                            'type-erro':'read-error',
                            'messege':''
                        })
            else:
                return Response({
                    'status':'error',
                    'type-error':'path-error',
                    'messege':'The "{path}" path not exits'.format(path=path)
                },status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'status':'error',
                'type-error':'page-not-found',
                'messege':'The page not exits'
            },status=status.HTTP_400_BAD_REQUEST)



    def post(self,request) -> (Response):

        """
          Se encarga de la creacion de archivos
          y carpetas de un proyecto
        """

        pageName = request.GET.get('page','')
        path = self.__getFilePath(request.get_full_path())
        resultObject = self.__getPageObjectModel(pageName)
        serializer = FileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        fileName = serializer.data['name']
        type = serializer.data['type']

        if resultObject:
            namespace = resultObject.namespace
            MEDIA_BASE_DIR = MEDIA_DIR + namespace + '\\' + path
            
            if os.path.exists(MEDIA_BASE_DIR):
                if os.path.isdir(MEDIA_BASE_DIR):
                    if type == 'file':
                        newFileDir = os.path.join(MEDIA_BASE_DIR,fileName) 
                        file = open(newFileDir,'w')
                        file.close()
                        return Response({
                            'status':'ok',
                            'messege':'The file is created !!',
                            'data':{
                                'name':fileName,
                                'type':'file',
                                'server-path':path,
                                'namespace':namespace
                                }
                            },status=status.HTTP_200_OK)

                    if type == 'dir':
                        mkdirPath = os.path.join(MEDIA_BASE_DIR,fileName)
                        if not os.path.exists(mkdirPath):
                            print('mkdir -->',mkdirPath)
                            os.mkdir(mkdirPath)
                            print('Creating mkdir')
                        else:
                            os.mkdir(mkdirPath + '- copy#'+str(random.randint(0,999999999999)))

                else:
                    print('Es un archivo')
            else:
                print('El archivo no existe')

        else:
            print('The page not exits')
            

        return Response('POST')




    def put(self,request) -> (Response):
        """
          Permite actualizar el nombre o el 
          contenido de un arvchivo
        """
        data = ({})
        pageName = request.GET.get('page')
        path = self.__getFilePath(request.get_full_path())
        page = self.__getPageObjectModel(pageName)
        serializer = UpdateFileSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        if page:
            MEDIA_BASE_DIR = MEDIA_DIR + page.namespace + '\\' + path
            if not os.path.isdir(MEDIA_BASE_DIR) and os.path.exists(MEDIA_BASE_DIR):
                fileName = serializer.data['fileName']
                content = serializer.data['content']
                data_ = serializer.uploadFile(
                    fileName=fileName,
                    content=content,
                    path=MEDIA_BASE_DIR
                )
                data = ({
                    'status':'ok',
                    'data':data_
                })

        return Response(data)










