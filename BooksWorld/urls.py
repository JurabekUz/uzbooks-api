from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

#drf-yasg
schema_view = get_schema_view(
    openapi.Info(
        title='UzBooks API',
        default_version='v1',
        description='Kitoblar haqida malumot va unga bildirilgan mashhur insonlar fikrlari',
        contact=openapi.Contact(email="contact@snippets.local"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('booksapi.urls')),
    path('docs/',schema_view.with_ui('swagger',cache_timeout=0), name='swagger-doc')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
