# bookstore/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger uchun schema view
schema_view = get_schema_view(
   openapi.Info(
      title="Bookstore API",
      default_version='v1',
      description="Bookstore API uchun dokumentatsiya",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@bookstore.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', include('books.urls')),
    path('api/users/', include('users.urls')),
    path('api/', include('carts.urls')),
    
    # Swagger uchun URL
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
]
