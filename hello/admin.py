from django.contrib import admin
from hello import models
# Register your models here.

class ControlUser(admin.ModelAdmin):
    '''自定义列表栏目'''
    #显示的字段
    list_display = ('user_name', 'psw', 'mail')
    #添加搜索条件
    search_fields = ('user_name', 'mail',)


class ControlArticle(admin.ModelAdmin):
    '''自定义列表栏目'''
    #显示的字段
    list_display = ('title', 'body', 'auth', 'create_time', 'update_time')
    #添加搜索条件
    search_fields = ('title', )
    #添加排序
    ordering = ('-create_time',)
    # #每页十行
    list_per_page = 10
    #分层
    list_filter = ('auth',)

admin.site.register(models.User, ControlUser)
admin.site.register(models.person)
admin.site.register(models.Article, ControlArticle)