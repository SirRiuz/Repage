
# Django
from django.db import models
from core.settings import BASE_DIR
from django.utils.crypto import get_random_string

#Python
import hashlib
import uuid
import os
import base64
import datetime



def namespacegenerator() -> (str):
    uuidRandom = str(uuid.uuid4().__str__().replace('-',''))
    randomText = get_random_string(length=50)
    date = str(datetime.datetime.now())
    print('date  ----> ',date)

    namespace = (uuidRandom+randomText+date).encode('ascii')
    return str(base64.b64encode(namespace))


class CustomPageManager(models.Manager):
    
    def create(self,**kwargs) -> (object):
        pageObject = self.model(
            user=kwargs['user'],
            name=kwargs['name'],
            namespace=namespacegenerator(),
            isAcces=kwargs.get('isAcces',True)
        )
        pageObject.save(using=self._db)
        os.mkdir(str(BASE_DIR)+'/media/'+pageObject.namespace+'/')
        return pageObject



class Page(models.Model):

    objects = CustomPageManager()

    user = models.ForeignKey(on_delete=models.CASCADE,to='accounts.User')
    name = models.CharField(max_length=100,null=False,unique=True)

    namespace = models.CharField(max_length=500,default=True)

    #namespace = models.CharField( max_length=100,default=str(uuid.uuid4().__str__().replace('-','')) + str(base64.b64encode(str(datetime.datetime.now()).encode('ascii') )))
    isAcces = models.BooleanField(default=True)

    date = models.DateField(auto_now_add=True)


    def delete(self):
        super().delete()
        namespaceDir = str(BASE_DIR)+'/media/'+self.namespace
        if os.path.exists(namespaceDir):
            shutil.rmtree(namespaceDir)
            os.rmdir(namespaceDir)


    def __str__(self) -> (str):
        return self.name

