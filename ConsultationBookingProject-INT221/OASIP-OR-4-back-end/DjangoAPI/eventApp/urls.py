from django.urls import re_path as url
from eventApp import user,event
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)


urlpatterns=[
    url(r'^events$',event.eventApi),
    url(r'^events/(?P<id>\d+)$',event.detailEventApi),

    url(r'^categories$',event.categoryApi),
    url(r'^categories/(?P<id>\d+)$',event.categoryApi),
    url(r'^categories/(?P<id>\d+)$',event.detailCategoryApi),
    url(r'^categories/(?P<id>\d+)/events',event.eventsCategoryApi),

    url(r'^users$',user.usersApi),
    url(r'^users/(?P<id>\d+)$',user.usersApi),
    url(r'^users/(?P<id>\d+)$',user.detailUserApi),
    url(r'^users/match', user.usersMatch),

    url(r'^login$',user.login),
    url(r'^logout$',user.logout),

    
]
