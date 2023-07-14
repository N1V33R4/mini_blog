from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('blog/', include('blog.urls')),
    path('', RedirectView.as_view(url='blog/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
