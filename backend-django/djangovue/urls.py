"""
URL configuration for djangovue project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from catalog.views import AlbumPhotosAPIView, UserInfoAPIView, UserViewSet, AddressViewSet, GeoViewSet, CompanyViewSet, TodoViewSet, PostViewSet, CommentViewSet, AlbumViewSet, PhotoViewSet, mark_todo_as_completed
from catalog import views

router = DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/company', CompanyViewSet)
router.register(r'api/geos', GeoViewSet)
router.register(r'api/address', AddressViewSet)
router.register(r'api/todos', TodoViewSet)
router.register(r'api/posts', PostViewSet)
router.register(r'api/comments', CommentViewSet)
router.register(r'api/albums', AlbumViewSet)
router.register(r'api/photos', PhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/users/<int:user_id>/todos/', views.UserTodosAPIView.as_view(), name='user_todos'),
    path('api/users/<int:user_id>/posts/', views.UserPostsAPIView.as_view(), name='user_posts'),
    path('api/users/<int:user_id>/albums/', views.UserAlbumsAPIView.as_view(), name='user_albums'),
    path('api/users/<int:user_id>/', UserInfoAPIView.as_view(), name='user_info'),
    path('api/users/<int:user_id>/albums/<int:album_id>/photos', AlbumPhotosAPIView.as_view(), name='album_photos'),
    path('api/todos/<int:pk>/complete/', mark_todo_as_completed, name='mark_todo_as_completed'),
    path('api/posts/<int:post_id>/comments/', views.get_comments, name='get_comments'),
]
