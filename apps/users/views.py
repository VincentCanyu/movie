# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import LoginForm
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm
from users.models import Movie_detail,Category

# Create your views here.
def index(req):
    categories=Category.objects.all()
    action_movies=Movie_detail.objects.filter(category__name='动作片')[:2]
    sicence_fiction_films=Movie_detail.objects.filter(category__name='科幻片').order_by('-add_time')[:2] ##这里想取后边2个数据，ORM不支持负索引。所以使用order_by
    affectional_movies=Movie_detail.objects.filter(category__name='爱情片')[:2]
    war_films=Movie_detail.objects.filter(category__name='战争片')[:2]
    love_action_movies=Movie_detail.objects.filter(category__name='爱情动作片')[:2]
    return render(req,'index.html',locals())

def logout_view(req):
    logout(req)
    return render(req,'index.html')

def register(req):
    if req.method!='POST':
        form=UserCreationForm()
    else:
        form=UserCreationForm(data=req.POST)
        if form.is_valid():
            new_user=form.save()
            authenticate_user=authenticate(username=new_user.username,password=req.POST['password1'])
            login(req,authenticate_user)
            return HttpResponseRedirect(reverse('index'))
    context={'form':form}
    return render(req,'register.html',context)