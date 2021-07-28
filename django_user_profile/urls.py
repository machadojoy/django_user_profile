
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('/', include(app.urls, namespace='app')),
    path('admin/', admin.site.urls),
]
