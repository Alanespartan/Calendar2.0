from django.contrib import admin
from django.urls import include,path
from django.conf.urls import url
import django.contrib.auth.views
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('root/', include('root.urls')),
    path('sesiones/', include('sesiones.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
