from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/post_latest/$', views.post_latest, name='post_latest'),
    url(r'^post/categories_list/$', views.category_list, name='category_list'),
    url(r'^post/categories_posts/$', views.category_posts, name='category_posts'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]