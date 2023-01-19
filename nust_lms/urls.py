from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include('base.urls'))
=======
    path('', include('base.urls')),
    path('__reload__/', include('django_browser_reload.urls')),
>>>>>>> a48c827e8bc6b52f9dc594a16fc79d5f970d3893
]
