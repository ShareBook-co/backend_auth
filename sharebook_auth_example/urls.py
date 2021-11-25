from django.contrib                 import admin
from django.urls                    import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from auth_example                   import views

urlpatterns = [
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
