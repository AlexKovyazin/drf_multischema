from django.urls import path, include
from rest_framework.routers import DefaultRouter

from revisions import views


router = DefaultRouter()
router.register(r'revisions', views.RevisionViewSet, basename='revision')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]
