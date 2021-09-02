from django.urls import path, include
from api_task import views

urlpatterns = [
    path('list/', views.ListTaskView.as_view()),
    path('create/', views.CreateTaskView.as_view()),
    path('<str:pk>/',
         views.RetrieveUpdateDestroyTaskView.as_view()),
]
