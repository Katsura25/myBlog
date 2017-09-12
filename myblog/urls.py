from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^books/$', views.PostListView.as_view(), name='posts'),
]
