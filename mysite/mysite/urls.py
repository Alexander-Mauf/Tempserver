from django.conf.urls import url
from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('sensordaten/', include('sensordaten.urls')),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls'))
]
