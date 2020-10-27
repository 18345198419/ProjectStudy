from django.conf.urls import url

from django.contrib.auth.views import auth_login

from .import views
urlpatterns = [
    # 登录页面
    url(r'^login/$', auth_login, {'template_name': 'users/login.html'})


]

