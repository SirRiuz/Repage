



# Rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer


# Django
from core.settings import MEDIA_DIR
#from ..core.settings import BASE_DIR


# Serailizers
from .serializers import UploadFileSerializer,PageSerializer


# Models
from ..models import Page



class FileUploadManager(APIView):

	#permission_classes = [ IsAuthenticated ]


	def __getPageObject(self,pageName:str) -> (object):
		"""
		  Retorna un obgeto de tipo Page si
		  este existe , de lo contrario retornar
		  un None
		"""
		pageObject = Page.objects.filter(name=pageName)
		if len(pageObject) > 0:
			return pageObject[0]
		return None

	
	def __saveFile(self,**kwargs) -> (bool):
		"""
		  Se encarga de guardar una lista 
		  de archivos en un namespace
		"""
		if kwargs['pageObject'].user == kwargs['user']:
			for fileItem in kwargs['files']:
				tempFileDir = MEDIA_DIR+kwargs['pageObject'].namespace+'\\'+kwargs['path']+'\\'+kwargs['files'][fileItem].name
				file = open(tempFileDir,'wb')
				file.write(kwargs['files'][fileItem].read())
				file.close()

			return True


		return False


	def post(self,request) -> (Response):
		"""
		  Este metodo permite la
		  subida de archivos y de
		  carpetas
		"""

		fileMap = request.FILES
		data = {}
		path = '/' if request.POST.get('path') == '' else request.POST.get('path').split('=')[1]
		user = request.user
		page = request.POST.get('page')

		result = self.__saveFile(
			pageObject=self.__getPageObject(page),
			user=user,
			files=fileMap,
			path=str(path).replace('/','\\')
		)

		if result:
			data = ({
				'status':'ok'
			})

		else:
			data= ({
				'status':'error',
				'type-error':'upload-error'
			})


		return Response(data)







