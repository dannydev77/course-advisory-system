from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('about/', views.about, name='about'),
    path('program/', views.course, name='program'),
    path('search/', views.search, name='search'),
    path('apply/<int:course_id>', views.apply_for_course, name='apply'),
    path('success/', views.on_success, name='success'),
]
