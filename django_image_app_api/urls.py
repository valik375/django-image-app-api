from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('adminhjsdo7f98bdsjlfy89yrsd/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
