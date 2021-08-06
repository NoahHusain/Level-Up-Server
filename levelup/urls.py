from django.conf.urls import include
from django.urls import path
from levelupapi.views import register_user, login_user
from rest_framework import routers
from levelupapi.views import GameTypeView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gametypes', GameTypeView, 'gametype')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
