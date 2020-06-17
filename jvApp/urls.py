from django.urls import include, path
from jvApp import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('wildcards', views.WildCardView)


urlpatterns = [
    path('', include(router.urls)),
]