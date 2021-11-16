from django.contrib import admin
from picture.models import TempPictureModel
# Register your models here.

class TestModelAdmin(admin.ModelAdmin):
    list_display = ('id','title','user','published_time')
    list_filter = ('title',)
    search_fields = ['title']

admin.site.register(TempPictureModel, TestModelAdmin)