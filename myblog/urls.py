from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('personal.urls')),
    url(r'^blog/', include('blog.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)