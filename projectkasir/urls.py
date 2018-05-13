from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('app_kasir.urls')),
    url(r'^accounts/', include('app_user.urls'))
]
