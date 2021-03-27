

# Rest_frameworl
from rest_framework import serializers

# Models
from ..models import Page


# Python 
import os



class UpdateFileSerializer(serializers.Serializer):

    fileName = serializers.CharField(required=False,default='')
    content = serializers.CharField(required=False,default='')

    def uploadFile(self,**kwargs):
        fileName = kwargs.get('fileName','')
        content = kwargs.get('content','')
        path = kwargs.get('path','')

        if content:
            file = open(path,'w')
            file.write(content)
            file.close()

        return ({
            'messege':'File update !!',
            'content':content
        })




class PageSerializerClass(serializers.ModelSerializer):
    class Meta(object):
        fields = '__all__'
        model = Page


class FileSerializer(serializers.Serializer):
    type = serializers.CharField(default='file')
    name = serializers.CharField(required=True)


class PageSerializer(serializers.Serializer):
    pageName = serializers.CharField(required=True)

    def create(self,data,model,user) -> (dict):
        query = ''
        pageName = data['pageName']
        pagesList = model.objects.filter(user=user)
        query = model.objects.filter(name=pageName)

        if  len(pagesList) + 1 > 5:
            return ({
                'status':'error',
                'type-error':'max-leng-pages',
                'messege':'Max pages !!'
            })

        if not query:
            if pageName != 'api':
                query = model.objects.create(
                    name=pageName,
                    user=user
                )
                return ({
                    'status':'ok',
                    'messege':'The page has been created !!'
                })
            return ({
                'status':'error',
                'type-error':'name-error',
                'messege':'You cannot use this name because it is already being used by the system'
            })
        else:
            return ({
                'status':'error',
                'type-error':'page-exits',
                'messege':'This name is already being used by another website'
            })




    def delete(self,pageName,model) -> (dict):
        data = ({
            'messege':'delete !!'
        })
        return data
        


class UploadFileSerializer(serializers.Serializer):

    file = serializers.FileField(required=False)
    path = serializers.CharField(max_length=10000,required=False)
    pageName = serializers.CharField(max_length=100,required=True)


