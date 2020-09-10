"""testtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from . import search

'''urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.conf.urls import url
 
from . import views
 
urlpatterns = [
    url(r'^$', views.hello),
]'''


urlpatterns = [
    url('^$',views.movieListsF, name="movieListF"),
    url('^moviePage/?P<count>([0-9]+)',views.movieLists, name="movieList"),
    url('^actorPage/?P<count>([0-9]+)',views.actorLists, name="actorList"),
    url(r'runoob/', views.runoob, name='runoob'),
    url(r'movie/(?P<name>[\u4e00-\u9fa50-9a-zA-Z -_]+)', views.movieInfo, name='movies'),
    url(r'actor/(?P<name>[\u4e00-\u9fa50-9a-zA-Z -_\\·\\.]+)', views.actorInfo, name='actors'),
    url(r'^search-post$',search.movieListSearch ),
    url(r'^search-post-2$',search.actorListSearch ),
    url(r'^search$',views.ss ,name='hoogle'),
    url(r'^search-movies$', search.searchMovieF ),
    url(r'^search-actors$', search.searchMovieF ),
    url(r'^search-comments$', search.searchMovieF ),
    url(r'^search-movies/?P<count>([0-9]+)/?P<count>(.+)$', search.searchMovie ,name="searchM"),
    url(r'^search-actors/?P<count>([0-9]+)/?P<count>(.+)$', search.searchActor ,name="searchA"),
    url(r'^search-comments/?P<count>([0-9]+)/?P<count>(.+)$', search.searchComment ,name="searchC")
]

'''urlpatterns = [
    url(r'runoob/', views.runoob),
]'''
