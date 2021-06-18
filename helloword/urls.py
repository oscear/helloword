"""helloword URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from helloword import view
from hello import views
from . import view, testdb
import xadmin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path("archive/<year>/<month>.html", views.home1),
    path("yoyo/", views.yoyo),
    path("page1/", views.page1),
    path("sonpage/", views.sonpage),
    url(r'^archive1/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2}).html$', views.home2),
    url(r'^$', view.index),
    url('^yoyo/$', view.yoyo),
    url('^demo/$', views.demo, name="demo_page"),
    url('^home/$', views.home, name="home_page"),
    url(r'^testdb/$', testdb.testdb),
    # url(r'^register/$', testdb.add_user),
    url(r'^update/$', testdb.update_psw),
    url(r'^delete/$', testdb.del_user),
    url(r'^mail/$', testdb.select_mail),
    url(r'^selall/$',testdb.select_all),
    url(r'^selfilter/$',testdb.sel_filtter),
    url(r'^selvalues/$', testdb.sel_values),
    url(r'^getjson/$',testdb.get_json),
    url(r'^mode_to_dict/$',testdb.mode_to_dict),
    url(r'^json_values/$',testdb.json_values),
    url(r'^name/$', views.user_name),
    url(r'^email/$', views.user_mail),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^reset/$', views.reset_psw),

]
