from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bgd_consultancy_app.urls')),
    path('account/', include('login_app.urls')),
    path('payment/', include('payment_app.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)