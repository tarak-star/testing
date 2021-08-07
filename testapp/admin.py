from django.contrib import admin
from testapp.models import Empmobnumbers

# Register your models here.
class AdminEmpmobnumbers(admin.ModelAdmin):
    list_display=['ename','emn','edegn','edept','emandal']
admin.site.register(Empmobnumbers,AdminEmpmobnumbers)
