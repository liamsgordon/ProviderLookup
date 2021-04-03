from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import BootstrapFilterView, info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BootstrapFilterView, name = 'home'),
    path('info/<int:slug>', info, name = 'info'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)