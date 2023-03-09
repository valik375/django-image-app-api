from rest_framework import routers
from .views import ImageView


router = routers.SimpleRouter()
router.register(r'', ImageView, basename='image')
urlpatterns = router.urls
