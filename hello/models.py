from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)
class person(models.Model):
    '''人员'''
    name=models.CharField(max_length=30)
    age=models.IntegerField()

    def __str__(self):
        return self.__doc__ + ":name>" + self.name

# 新增一张用户表，表名为user 字段user_name, psw ,mail 都是字符串类型
class User(models.Model):
    '''用户'''
    user_name = models.CharField(max_length=30,
                                 primary_key=True)   # 设置为主键
    psw = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)

    def __str__(self):
        return self.__doc__ + ":user_name->" + self.user_name

class Article(models.Model):
    '''文章'''
    title = models.CharField(max_length=30, verbose_name="标题")  # 标题
    body = models.TextField(verbose_name="正文")                # 正文
    auth = models.CharField(max_length=10, verbose_name="作者")   # 作者
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.__doc__ + "title->" + self.title
    class Meta:
        verbose_name_plural="文章列表"