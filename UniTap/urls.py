
from django.contrib import admin
from django.urls import path,include
from django.conf import settings # new
from django.conf.urls.static import static
from django.conf.urls import handler404
handler404 = 'mainapp.views.view_404'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mainapp.urls')),
    path('tinymce/', include('tinymce.urls')),
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
