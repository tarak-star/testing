from django.db import models

# Create your models here.
class Empmobnumbers(models.Model):
    DEPT_CHOICES=(('APSHCL','APSHCL'),('PR','PR'),('RWS','RWS'))
    ename=models.CharField("name of the employee",max_length=30)
    emn=models.IntegerField("Mobile Number")
    edegn=models.CharField("Designation",max_length=30)
    edept=models.CharField("Name of the Department",max_length=10,choices=DEPT_CHOICES,default='apshcl')
    emandal=models.CharField("Name of the Mandal",max_length=20)
