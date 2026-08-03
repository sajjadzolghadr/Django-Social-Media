from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.post_create,name='create'),
    path('like/<int:post_id>/', views.like_post,name='like'),
    path('comment/<int:post_id>/', views.add_comment,name='add_comment'),
    path('save/<int:post_id>/', views.save_post, name='save_post'),
    path('unsave/<int:post_id>/', views.unsave_post, name='unsave_post'),

]