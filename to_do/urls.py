from django.urls import path
from to_do import views


urlpatterns = [
    path('',views.index,name='index'),
    path('update/<str:pk>/', views.update,name='update_todo'),
    path('delete/<str:pk>/', views.delete,name='delete'),

]

