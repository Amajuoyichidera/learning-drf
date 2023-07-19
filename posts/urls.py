from django.urls import path
from . import views

urlpatterns = [
    path('homepage/',views.homepage, name='posts_home'),
    path('',views.PostListCreateView.as_view(), name='list_post'),
    path('<int:pk>/',views.PostRetrieveUpdateDeleteView.as_view(),name='post_detail'),
]