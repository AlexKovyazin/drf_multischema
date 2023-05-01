from django.urls import path, include
from rest_framework.routers import DefaultRouter

from base_models import views


router = DefaultRouter()
router.register(r'articles', views.ArticleViewSet, basename='article')
router.register(r'balances', views.BalanceViewSet, basename='balance')
router.register(r'shops', views.ShopViewSet, basename='shop')

urlpatterns = [
    path('', include(router.urls))
]
