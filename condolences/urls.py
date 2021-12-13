from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='condolences'),
    path('<int:id>/', views.post_details, name='post_details'),
    path('add/', views.add_post, name='add_post'),
    path('edit/<int:id>/', views.edit_post, name='edit_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
]