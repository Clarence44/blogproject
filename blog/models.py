from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length = 70)

    body = models.TextField()

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    #文章摘要
    excerpt = models.CharField(max_length = 200, blank = True)

    #分类一对多，标签多对多
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank = True)

    #文章作者，这里User是从Django.contrib.auth.models导入
    #Django.contrib.auth 是Django内置应用，专门用于处理网站用户的注册、登陆等流程，User是Django为我们已经写好的用户模型
    #通过ForeignKey把文章和User关联起来
    author = models.ForeignKey(User)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']
