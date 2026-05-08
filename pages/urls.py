from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('about/<int:year>/', views.about, name='about_year'),  # ✅ Path Converter
    path('contact/', views.contact, name='contact'),
    path('raw/', views.plain_response, name='plain'),           # ✅ HttpResponse demo
]