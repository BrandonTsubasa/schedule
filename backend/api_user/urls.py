from django.urls import path, include
from api_user import views

app_name = 'user'


urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('myself/', views.ManageUserView.as_view(), name='myself'),
    path('list/', views.ListUserView.as_view(), name='list'),
    path('<str:pk>/', views.DeleteUserView.as_view()),
]
