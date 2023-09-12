from django.urls import path
from . import views

app_name = 'cafe'

urlpatterns = [
    # Add cafe page (placed before the cafe home page pattern)
    path('add/', views.AddCafe.as_view(), name='add'),
    
    # Cafe home page
    path('', views.IndexClassView.as_view(), name='index'),
]