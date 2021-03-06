from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),

    path('profile/', views.profile, name='profile'),
    path('get_pdf/', views.pdf_report, name='get_pdf'),
    path('edit/', views.edit_profile, name='edit'),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
