from django.conf.urls import url,include
from django.contrib.auth.views import login
from .views import logout_view,register

urlpatterns = [
    url(r'^login$',login,{'template_name':'login.html'},name='login'),
    url(r'^logout$',logout_view,name='logout'),
    url(r'^register$',register,name='register'),
]
