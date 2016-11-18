<<<<<<< HEAD
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from exile_ui.admin import admin_site
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    #url(r'^$', 'huella.views.index', name='index'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(admin_site.urls)),
    #url(r'^empresa/', include('empresa.urls')),
    #url(r'^norma/', include('norma.urls')),
    #url(r'^notificacion/', include('notificacion.urls')),
    
    url(r'^nested_admin/', include('nested_admin.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from exileui.admin import exileui
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    #url(r'^$', 'huella.views.index', name='index'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(exileui.urls)),
    #url(r'^empresa/', include('empresa.urls')),
    #url(r'^norma/', include('norma.urls')),
    #url(r'^notificacion/', include('notificacion.urls')),

    url(r'^nested_admin/', include('nested_admin.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> d4a43d94c0aa6b0b9855c268cd630ce06cd3af9c
