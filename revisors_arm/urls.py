from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('revisions/', include('revisions.urls')),
    path('base/', include('base_models.urls')),
]
