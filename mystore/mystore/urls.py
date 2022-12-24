from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('store.urls'), name='home'),
    path('users/', include('users.urls'), name='users'),
    path('orders/', include('orders.urls'), name='orders'),
    path('admin/', admin.site.urls),
    path('api/password_reset/',
        include('django_rest_passwordreset.urls', namespace='password_reset'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)