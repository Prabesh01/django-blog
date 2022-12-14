from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(),name='post-delete'),
    path('u/<str:username>/', views.UserPostListView.as_view(),name='user-posts'),
    path('new/', views.PostCreateView.as_view(),name='post-create'),
    path('about/', views.about,name='blog-about'),
]