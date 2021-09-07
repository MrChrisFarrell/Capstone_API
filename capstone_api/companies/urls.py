from django.urls import path
from . import views

urlpatterns = [
    path('company/', views.CompanyList.as_view()),
    path('company/<int:pk>/', views.CompanyDetail.as_view()),
    path('promotion/', views.PromotionList.as_view()),
    path('promotion/<int:pk>/', views.PromotionDetail.as_view()),
    path('employee/', views.EmployeeList.as_view()),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view()),
    path('complatlong/', views.CompanyLatLongList.as_view()),
    path('emplatlong/', views.EmployeeLatLongList.as_view()),
    path('emplatlong/get/', views.EmployeeLatLongDetail.as_view()),
]