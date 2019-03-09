# _*_ encoding:utf-8 _*_
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"类型名")
    movie_nums = models.IntegerField(default=0, verbose_name=u'电影数量')

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Movie_detail(models.Model):
    category= models.ManyToManyField(Category, verbose_name=u"类型")
    name = models.CharField(max_length=100, verbose_name=u"电影名")
    desc = models.TextField(verbose_name=u"电影描述")
    director =models.CharField(max_length=100, verbose_name=u"导演")
    to_star= models.CharField(max_length=100, verbose_name=u"主演")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    image=models.ImageField(upload_to='static/images',max_length=300, verbose_name=u"封面图")
    add_time=models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")

    def __str__(self):
        return self.name