from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user/<int:user_id>/', views.user_details, name='user_details'),
    path('users/', views.user_list, name='user_list'),  # Новый маршрут для списка пользователей
    path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Страница выхода
]
