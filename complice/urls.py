from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^goals/$', views.goals, name='goals'),
    url(r'^test/$', views.test_view, name='test'),
]


