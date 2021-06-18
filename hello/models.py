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

class Bank(models.Model):
    '''银行信息'''
    bank_name = models.CharField(max_length=50, verbose_name="银行")
    city = models.CharField(max_length=50,verbose_name ="城市")
    point = models.CharField(max_length=60,verbose_name="网点")
    class Meta:
        verbose_name_plural = '银行信息'
    def __str__(self):
        return  self.bank_name

class Cardinfo(models.Model):
    '''卡信息'''
    card_id = models.CharField(max_length=60, verbose_name='卡号')
    card_user = models.CharField(max_length=30, verbose_name='持有人姓名')
    info = models.ForeignKey(Bank,on_delete=models.CASCADE,verbose_name='选择银行')
    class Meta:
        verbose_name_plural = '卡号信息'
    def __str__(self):
        return self.__doc__ +"card_id->" + self.card_id

class Auther(models.Model):
    '''作者'''
    name = models.CharField(max_length=10, verbose_name="作者")
    mail = models.CharField(max_length=30, verbose_name="邮箱")
    city = models.CharField(max_length=10, verbose_name="城市")
    class Meta:
       verbose_name_plural = '作者'

    def __str__(self):
        return self.name

class Book(models.Model):
    '''书籍详情'''
    book_name = models.CharField(max_length=50, verbose_name="书名")
    auth = models.ManyToManyField(Auther, verbose_name="作者")
    class Meta:
       verbose_name_plural = '书籍详情'

    def __str__(self):
        return self.book_name

# models.py

from django.db import models

# Create your models here.

class Card(models.Model):
    '''银行卡 基本信息'''
    card_id = models.CharField(max_length=30, verbose_name="卡号", default="")
    card_user = models.CharField(max_length=10, verbose_name="姓名", default="")
    add_time = models.DateField(auto_now=True, verbose_name="添加时间")
    class Meta:
        verbose_name_plural = '银行卡账户'
        verbose_name = "银行卡账户_基本信息"
    def __str__(self):
        return self.card_id

class CardDetail(models.Model):
    '''银行卡 详情信息'''
    card = models.OneToOneField(Card,
                               on_delete=models.CASCADE,
                               verbose_name="卡号"
                                )
    tel = models.CharField(max_length=30, verbose_name="电话", default="")
    mail = models.CharField(max_length=30, verbose_name="邮箱", default="")
    city = models.CharField(max_length=10, verbose_name="城市", default="")
    address = models.CharField(max_length=30, verbose_name="详细地址", default="")

    class Meta:
        verbose_name_plural = '个人资料'
        verbose_name = "账户_个人资料"

    def __str__(self):
        return self.card.card_user

class Student(models.Model):
    '''学生成绩'''
    student_id = models.CharField(max_length=30, verbose_name="学号")
    name = models.CharField(max_length=30, verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    score = models.IntegerField(verbose_name="分数")

    class Meta:
        verbose_name = "学生成绩"
        verbose_name_plural = verbose_name