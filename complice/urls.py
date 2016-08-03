from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^createroom$', views.createroom, name='createroom'),
    url(r'^rooms$', views.rooms, name='rooms'),
    url(r'^features$', views.features, name='features'),
    url(r'^legalstuff$', views.legalstuff, name='legalstuff'),
    url(r'^faq$', views.faq, name='faq'),
    url(r'^newsletter$', views.newsletter, name='newsletter$'),
    url(r'^faq$', views.faq, name='faq'),
    url(r'^Fivapr/$', views.fivapr, name='fivapr'),
    url(r'^Fivapr/today/$', views.fivapr_today, name='fivapr_today'),
    url(r'^Fivapr/settings/$', views.fivapr_settings, name='fivapr_settings'),
    url(r'^Fivapr/reviews/$', views.fivapr_reviews, name='fivapr_reviews'),
    url(r'^Fivapr/reviews/2016/Jul/$', views.fivapr_reviews_2016_Jul, name='fivapr_reviews_2016_Jul'),
    url(r'^Fivapr/reviews/2016/weeks/30/$', views.fivapr_reviews_2016_week_30, name='fivapr_reviews_2016_week_30'),
    url(r'^Fivapr/goals/$', views.fivapr_goals, name='fivapr_goals'),
    url(r'^Fivapr/refer/$', views.fivapr_refer, name='fivapr_refer'),
]