"""定义learning_logs的URL模式"""

from django.conf.urls import url
from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 显示所有主题
    url(r'topics/$', views.topics, name='topics'),

    # 显示特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # 用户添加主题页面
    url(r'new_topic/$', views.new_topic, name='new_topic'),

    # 用户添加新条目页面
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # 用户编辑条目信息
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry')
]
