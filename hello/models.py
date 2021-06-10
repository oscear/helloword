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