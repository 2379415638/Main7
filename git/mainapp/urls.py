from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^user/$',views.user,name="user"),
    url(r'^login/$',views.login,name="login"),
    url(r'^logout/$',views.logout,name="logout"),
    url(r'^send/(.*?)/(.*?)/(.*?)/$',views.send,name="send"),
    url(r'^content/(\d+)',views.content,name="content"),
]
app_name="mainapp"