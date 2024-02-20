from django.shortcuts import render
from rest_framework import viewsets, status
from .models import User, Todo, Post, Comment, Album, Photo, Geo, Company, Address
from .serializer import UserSerializer, TodoSerializer, PostSerializer, CommentSerializer, AlbumSerializer, PhotoSerializer, GeoSerializer, AddressSerializer, CompanySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view

class GeoViewSet(viewsets.ModelViewSet):
    queryset = Geo.objects.all()
    serializer_class = GeoSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            # Kullanıcı verilerini al
            user_data = user_serializer.validated_data

            # Adres verilerini al
            address_data = user_data.pop('address', None)

            # Şirket verilerini al
            company_data = user_data.pop('company', None)

            # Adres oluştur
            address_serializer = AddressSerializer(data=address_data)
            if address_serializer.is_valid():
                address_instance = address_serializer.save()
            else:
                return Response(address_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # Şirket oluştur
            company_serializer = CompanySerializer(data=company_data)
            if company_serializer.is_valid():
                company_instance = company_serializer.save()
            else:
                return Response(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # Kullanıcıyı oluştur
            user_instance = User.objects.create(
                address=address_instance,
                company=company_instance,
                **user_data
            )

            # Kullanıcı verilerini serialize et
            serialized_user = UserSerializer(user_instance)

            return Response(serialized_user.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
class UserTodosAPIView(APIView):
    def get(self, request, user_id):
        todos = Todo.objects.filter(user_id=user_id)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserInfoAPIView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=True, methods=['post'])
    def mark_as_completed(self, request, pk=None):
        todo = self.get_object()
        todo.completed = True
        todo.save()
        serializer = self.get_serializer(todo)
        return Response(serializer.data)

class UserPostsAPIView(APIView):
    def get(self, request, user_id):
        posts = Post.objects.filter(user_id=user_id)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
       
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    
def get_comments(request, post_id):
    comments = Comment.objects.filter(post_id=post_id)
    comments_data = [{'name': comment.name, 'text': comment.text} for comment in comments]
    return JsonResponse(comments_data, safe=False)
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UserAlbumsAPIView(APIView):
    def get(self, request, user_id):
        albums = Album.objects.filter(user_id=user_id)
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumPhotosAPIView(APIView):
    def get(self, request, user_id, album_id):
        photos = Photo.objects.filter(album__user_id=user_id, album_id=album_id)
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

@api_view(['PUT'])
def mark_todo_as_completed(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        completed = not todo.completed  # Toggle completed status
        serializer = TodoSerializer(todo, data={'completed': completed}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
