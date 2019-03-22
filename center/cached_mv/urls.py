from rest_framework import routers

from . import views

router = routers.SimpleRouter()

# simple views of those derived from ModelViewSet:
router.register('clients', views.ClientViewSet, 'client')
router.register('belongings', views.BelongingViewSet, 'belonging')

urlpatterns = router.urls