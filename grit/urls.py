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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)