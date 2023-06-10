from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('index.urls')),
    path('api/v1/', include('app_car_model.urls')),

    path('admin/', admin.site.urls),
]

from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)