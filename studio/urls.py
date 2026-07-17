from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('commission/<int:id>/', views.commission_detail, name='commission_detail'),
    path('submit/', views.submit_commission, name='submit_commission'),
    path('success/', views.success, name='success'), 
     # API endpoints
    path('api/artworks/', views.api_artworks, name='api_artworks'),
    path('api/artworks/<int:id>/', views.api_artwork_detail, name='api_artwork_detail'),
    path('api/commission/', views.api_submit_commission, name='api_submit_commission'),
]