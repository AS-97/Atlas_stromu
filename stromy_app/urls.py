from django.urls import path
from . import views

urlpatterns = [
    path('', views.seznam_stromu, name='seznam_stromu'),
    path('<int:strom_id>/', views.detail_stromu, name='detail_stromu'),
]