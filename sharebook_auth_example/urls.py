from django.contrib                 import admin
from django.urls                    import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from auth_example                   import views

urlpatterns = [
    path('admin/',         admin.site.urls),
    path('login/',         TokenObtainPairView.as_view()), 
    path('refresh/',       TokenRefreshView.as_view()), 
    path('veryfyToken',    views.VerifyTokenView.as_view()),
    path('user/',          views.UserCreateView.as_view()), 
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('book/',          views.bookView.BookListCreateView.as_view()),
    path('book/<int:pk>/', views.bookView.BooksView.as_view()),
]
