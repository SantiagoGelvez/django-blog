from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('api/', views.post_list_api, name='post_list_api'),
    path('api/<int:id>/', views.post_detail_api, name='post_detail_api'),
]
