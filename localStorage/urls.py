from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('allauth.urls')),
    path('account/', include('account.urls', namespace='account')),
    path('dashboard/', include('video.urls', namespace='dashboard')),
    # path('payment/', include('payment.urls', namespace='payment')),
    # path("stripe/", include("djstripe.urls", namespace="djstripe")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)