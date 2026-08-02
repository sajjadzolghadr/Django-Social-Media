from django.urls import path
from . import views

urlpatterns = [
    path('create',views.post_create,name='create'),
    path('like/<int:post_id>/', views.like_post, name='like')

]