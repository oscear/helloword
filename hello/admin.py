from django.contrib import admin
from hello import models
# Register your models here.

class ControlUser(admin.ModelAdmin):
    '''自定义列表栏目'''
    #显示的字段
    list_display = ('user_name', 'psw', 'mail')
    #添加搜索条件
    search_fields = ('user_name', 'mail',)


admin.site.register(models.User, ControlUser)
admin.site.register(models.person)