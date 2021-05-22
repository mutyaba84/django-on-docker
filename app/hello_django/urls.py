from django.contrib import admin
from django.urls import path, include

from task.views import VariableViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"Variable", VariableViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
]
