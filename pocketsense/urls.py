from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Pocketsense API",
      default_version='v1',
      description="API for managing expenses, payments, and concerns for college students",
      contact=openapi.Contact(email="contact@pocketsense.local"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('expenses.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
