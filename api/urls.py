from django.urls import re_path, path
from django.conf.urls import include
from django.conf import settings

from rest_framework.permissions import AllowAny

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Ares web API",
      default_version='v1',
      description="Ares fightclub crm API",
      terms_of_service="https://web-ares.ru",
      contact=openapi.Contact(email=""),
      license=openapi.License(name=""),
   ),
   public=True,
   permission_classes=(AllowAny,),
   url=settings.SITE_URL,
)


urlpatterns = [
    re_path(r'v1/', include('api.v1.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

