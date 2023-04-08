from django.urls import path

from . import views

app_name = 'car_price_estimator'

urlpatterns = [
    path('', views.index, name='index'),
    path('estimate/', views.estimate, name='estimate'),
    path('about/', views.about, name='about'),
]
