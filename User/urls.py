from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:id>', views.Profile_page, name='profile'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout.as_view(), name='logout'),
    path('login/', views.login.as_view(), name='login'),
]