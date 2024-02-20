from rest_framework import serializers
from .models import User, Geo, Address, Company, Todo, Comment, Post,Album, Photo

class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    geo = GeoSerializer()

    class Meta:
        model = Address
        fields = '__all__'
    def create(self, validated_data):
        geo_data = validated_data.pop('geo')
        geo_instance = Geo.objects.create(**geo_data)
        address_instance = Address.objects.create(geo=geo_instance, **validated_data)
        return address_instance

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    company = CompanySerializer()

    class Meta:
        model = User
        fields = '__all__'
    

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
