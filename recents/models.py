
# Django
from django.db import models




class RecentItem(models.Model):

    page = models.ForeignKey('pages.Page',on_delete=models.CASCADE)
    path = models.CharField(max_length=100,null=False)
    nameDir = models.CharField(max_length=100,default='Undefined')
    typeFile = models.CharField(max_length=50,default='File')

    date = models.DateTimeField(auto_now_add=True)


    def str(self) -> (str):
        return self.path

