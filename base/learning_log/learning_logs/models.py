from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    """用户学习主题"""
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        """返回字符串类型"""
        return self.text


class Entry(models.Model):
    """学到某个主题的具体知识"""
    topic = models.ForeignKey(Topic, models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回字符串类型"""
        return str(self.text[:50]) + "..."
