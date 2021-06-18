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

class ControlBank(admin.ModelAdmin):
    # 显示的字段
    list_display = ["bank_name", "city", "point"]

class ControlCardInfo(admin.ModelAdmin):
    # 显示的字段
    list_display = ["card_id", "card_user", "info"]

class ControlAuther(admin.ModelAdmin):
    # 显示的字段
    list_display = ["name", "city", "mail"]

class ControlBook(admin.ModelAdmin):
    # 显示的字段
    list_display = ["book_name", "作者"]

    # 定义一个方法，遍历book的auth，然后用列表返回
    def 作者(self, obj):
        return [a.name for a in obj.auth.all()]
class MoreInfo(admin.TabularInline):
    '''StackedInline是纵向显示，TabularInline是横线显示'''
    model = models.CardDetail

@admin.register(models.Card)
class ControlCard(admin.ModelAdmin):
    list_display = ["card_id", "card_user", "add_time"]

    # 在Card页面显示更多信息CardDetail
    inlines = [MoreInfo]

admin.site.register(models.User, ControlUser)
admin.site.register(models.person)
admin.site.register(models.Article, ControlArticle)
admin.site.register(models.Bank, ControlBank)
admin.site.register(models.Cardinfo, ControlCardInfo)
admin.site.register(models.Auther, ControlAuther)
admin.site.register(models.Book, ControlBook)
