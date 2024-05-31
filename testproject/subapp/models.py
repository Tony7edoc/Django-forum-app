from django.db import models

# Create your models here.
class postmodel(models.Model):
    class Meta(object):
        db_table="table1"
    
    name=models.CharField('name',max_length=50,null=False,blank=False)