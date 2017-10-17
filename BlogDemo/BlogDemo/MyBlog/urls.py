# -*- coding:utf-8 -*-
from rest_framework import routers
import views

router = routers.SimpleRouter()
router.register(r'capacityratio', views.CapacityRatioLogViewSet, base_name='capacitylog')
urlpatterns = router.urls
