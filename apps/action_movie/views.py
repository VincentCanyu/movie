# _*_ encoding:utf-8 _*_
from django.shortcuts import render,HttpResponse
from users.models import Movie_detail,Category
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
import json


# Create your views here.
# 影片详情页
def movie_detail(req,movie_id):
    categories=Category.objects.all()
    movie=Movie_detail.objects.get(id=movie_id)  ##取到该电影
    movie_desc=movie.desc[:100]    ##电影详情默认只显示100字符
    category=Category.objects.filter(movie_detail__id=movie_id)[0]  ##该电影所属的类别，所属类别可能是多个。所以使用filter，为了取到其相关电影，取其第一个类别
    movies=Movie_detail.objects.filter(category__name=category)[:3]  ##该类别相关电影
    return render(req,'movie_detail.html',locals())

# 影片描述展开
def movie_detail_spread(req):
    id=req.POST.get('nid')  ##取Ajax传来的id
    movie=Movie_detail.objects.get(id=id) ##取到该id的电影对象
    movie_desc=movie.desc  ##该电影的描述信息
    return HttpResponse(movie_desc)

#影片描述收起
def movie_detail_retract(req):
    id=req.POST.get('nid')
    movie=Movie_detail.objects.get(id=id)
    movie_desc=movie.desc[:100]
    return HttpResponse(movie_desc)

def all_movies(req,category_id):
    categories=Category.objects.all()
    all_movies=Movie_detail.objects.filter(category__id=category_id)  ##此类型id的所有电影

    try:   ##分页
        page = req.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(all_movies,5,request=req)
    movies = p.page(page)

    return render(req,'all_movies.html',locals())





    # action_movies=Movie_detail.objects.filter(category__name='动作片')[:3]  ##相关影片
    # affectional_movies=Movie_detail.objects.filter(category__name='爱情片')[:3]
    # science_fiction_movies=Movie_detail.objects.filter(category__name='科幻片')[:3]
    # war_films=Movie_detail.objects.filter(category__name='战争片')[:3]
    # love_action_movies=Movie_detail.objects.filter(category__name='爱情动作片')[:3]