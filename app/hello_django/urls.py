from upload.views import image_upload
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from task.views import VariableViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"Variable", VariableViewSet)


urlpatterns = [
    path("", image_upload, name="upload"),
    path("admin/", admin.site.urls),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
