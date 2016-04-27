from django.conf.urls import url
from blog import views

urlpatterns  =[
#01091294131
    url(r'^$', views.index),
    url(r'^post$', views.post_list, name="post_list"),
    url(r'^post/(?P<pk>\d+)$', views.post_detail, name="post_detail"),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<post_pk>\d+)/comments/new/$', views.comment_new, name="comment_new"),
]

