from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('student-list/', views.StudentList, name="student-list"),
	path('student-detail/<str:pk>/', views.StudentDetail, name="student-detail"),
	path('student-create/', views.StudentCreate, name="student-create"),

	path('student-update/<str:pk>/', views.StudentUpdate, name="student-update"),
	path('student-delete/<str:pk>/', views.StudentDelete, name="student-delete"),
]