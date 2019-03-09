# _*_ encoding:utf-8 _*_
from django.conf.urls import url
from .views import movie_detail,movie_detail_spread,movie_detail_retract,all_movies

urlpatterns = [
    url(r'^movie_detail/(?P<movie_id>\d+)$',movie_detail,name='movie_detail'),  ##电影详情
    url(r'^movie_detail/movie_detail_spread$',movie_detail_spread,name='movie_detail_spread'),  ##ajax实现展开，url前面必须是movie_detail/，或许是因为是在当前页面修改的，修改之后页面还停留在此。因此url前缀不能改变。
    url(r'^movie_detail/movie_detail_retract$',movie_detail_retract,name='movie_detail_retract'),
    url(r'^all_movies/(?P<category_id>\d+)$',all_movies,name='all_movies'),  ##所有电影
]
