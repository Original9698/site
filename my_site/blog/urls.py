from django.urls import path
from blog import views

urlpatterns = [
    path('', views.post_menu),
    path('<str:name_post>/', views.blog_posts, name='posts_name'),
]
