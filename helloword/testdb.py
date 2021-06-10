from django.http import JsonResponse, HttpResponse
from hello.models import *
import random
from django.core import serializers
import json
from django.forms.models import model_to_dict

# 数据库操作
def testdb(request):
    test1 = Test(name='奥克斯'+str(random.randrange(0,9999,1)))
    test1.save()
    return HttpResponse("数据库hello_test添加name成功！看去看看吧")

#新增用户
def add_user(request):
    test1 = User(user_name='奥斯卡',
                       psw="123456789")
    test1.save()
    return HttpResponse("奥斯卡用户创建成功！看去看看吧")


def update_psw(requests):
    # 修改其中一个user_name='yoyo5'的字段，再save，相当于SQL中的UPDATE
    test2 = User.objects.get(user_name='yoyo5')
    test2.psw = '99999'
    test2.save()

    # # 另一方式
    # Test.objects.filter(id=1).update(name='google')
    # #修改所有列
    # Test.objects.all().update(name='chrome')
    return HttpResponse("<p>密码修改成功</p>")

def del_user(requests):
    #删除yoyo数据
    test=User.objects.get(user_name='yoyo')
    test.delete()

    # #另一种方式
    # Test.objects.filter(id=1).delete()
    # #删除全部
    # Test.objects.all().delete()
    return HttpResponse("<b>删除成功</b>")
# 查询数据
def select_mail(request):

    # 方法1 可以查询单个结果直接获取mail值
    test = User.objects.get(user_name='yoyo').psw

    # 方法2 filter相当于SQL中的WHERE，可设置条件过滤结果
    # test4 = User.objects.filter(user_name='yoyo')

    # 查询结果是list，取下标后，获取mail字段的值
    # m = test4[0].mail

    return HttpResponse("<p>查询结果：%s</p>" % test)


def select_all(requests):
    test = User.objects.all()
    users = ""
    psw = ""
    mail = ""
    for i in test:
        users += "  " + i.user_name
        psw += "  " + i.psw
        mail += "  " + i.mail

    return HttpResponse("<p>查询的user结果是:%s</p>"
                        "<p>查询的pws结果是：%s</p>"
                        "<p>查询的mail结果是:%s</p>" % (users, psw, mail))

def sel_filtter(request):
    '''根据查询条件查询对应的mail'''
    r=""
    ret = User.objects.filter(user_name="yoyo", psw="12345")
    try:
        r = ret[0].mail
    except:
        r = "null"
    return HttpResponse("<P>查询的邮箱结果是：%s</P>" %r)

def sel_values(request):
    '''获取字典'''
    r = " "
    ret=User.objects.all().values()
    for i in ret:
        r += str(i)
    return HttpResponse('<p>查询结果是：%s</p>' %r)


def get_json(request):
    '''将查询返回json'''
    data={}
    a = User.objects.all()
    data['result'] = json.loads(serializers.serialize("json", a))
    return JsonResponse(data)

def mode_to_dict(request):
    '''把返回值转成dict'''
    ret = User.objects.all()
    json_list=[]
    for i in ret:
        json_dict = model_to_dict(i)
        json_list.append(json_dict)
        #safe=true只能传字典，false随意
    return JsonResponse(json_list,safe=False)
def json_values(request):
    '''获取可迭代对象转list'''
    data={}
    ret=User.objects.all().values()
    data['data'] = list(ret)
    return JsonResponse(data, safe=False,json_dumps_params={'ensure_ascii':False})