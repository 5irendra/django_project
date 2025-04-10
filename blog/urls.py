from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)
from . import views


urlpatterns = [
    path("", PostListView.as_view(), name="blog-home"),  # views.home
    path("post/<str:username>", UserPostListView.as_view(), name="user-posts"),   
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("about/", views.about, name="blog-about"),
]

# <app>/<model>_<viewtype>.html -- (PostDetailView)error or name that is webpage loking for
# <app>/<model>_form.html --- PostCreateView
