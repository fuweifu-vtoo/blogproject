from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Image(models.Model):
    """
    标签 Tag 也比较简单，和 Category 一样。
    再次强调一定要继承 models.Model 类！
    """
    href = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title
#访问网站的ip地址和次数
class Userip(models.Model):
    ip=models.CharField(verbose_name='IP地址',max_length=30)    #ip地址
    count=models.IntegerField(verbose_name='访问de次数',default=0) #该ip访问次数
    class Meta:
        verbose_name = '访问de用户信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.ip

#各页面访问次数
class VisitNumber(models.Model):
    page_name = models.CharField(verbose_name='页面de名称',max_length=30,default='home')
    count = models.IntegerField(verbose_name='页面de访问次数',default=0) #网站访问总次数
    class Meta:
        verbose_name = '各页面de访问次数'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.count)
