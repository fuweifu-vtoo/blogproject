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
