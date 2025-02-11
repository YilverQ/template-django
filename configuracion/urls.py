from django.contrib import admin
from django.urls    import path

from apps.frontend.views        import inicio

from .api import api

urlpatterns =   [
                    path('',            inicio,             name = 'inicio'             ),
                    path("admin/",      admin.site.urls),
                    path("",            api.urls)
                ]
