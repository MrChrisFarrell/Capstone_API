from django.urls import path
from . import views

urlpatterns = [
    path('company/', views.CompanyList.as_view()),
    path('company/<int:pk>/', views.CompanyDetail.as_view())
]