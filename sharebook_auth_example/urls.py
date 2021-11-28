from django.contrib                 import admin
from django.urls                    import path, include, re_path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from auth_example                   import views

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Documentación de API Sharebook",
      default_version='v0.1',
      description="Documentación pública de API de ShareBook",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="andres.afm72@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/',                admin.site.urls),
    path('login/',                TokenObtainPairView.as_view()), 
    path('refresh/',              TokenRefreshView.as_view()), 
    path('veryfyToken',           views.VerifyTokenView.as_view()),
    path('user/',                 views.UserCreateView.as_view()), 
    path('user/<int:pk>/',        views.UserDetailView.as_view()),
    path('user/update/<int:pk>/', views.UserUpdateView.as_view()),
    path('user/remove/<int:pk>/', views.UserDeleteView.as_view()),
    path('book/',                 views.BookListCreateView.as_view()),
    path('book/<int:pk>/',        views.BookDetailView.as_view()),
    path('book/update/<int:pk>/', views.BookUpdateView.as_view()),
    path('book/remove/<int:pk>/', views.BookDeleteView.as_view()),
]
