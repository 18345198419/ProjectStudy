from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def logout_view(request):
    """用户注销"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    """用户注册"""
    if request.method != 'POST':
        # 显示空的注册表
        form = UserCreationForm()
    else:
        # 提交注册信息，进行数据处理
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，在重定向到主页
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
