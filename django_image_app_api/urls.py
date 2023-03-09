from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django_image_app_api import settings

urlpatterns = [
    path('adminhjsdo7f98bdsjlfy89yrsd/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('images/', include('image_app.urls'))
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
