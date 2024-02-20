from django.db import models

# Create your models here.
from django.db import models

class Geo(models.Model):
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

class Address(models.Model):
    street = models.CharField(max_length=100)
    suite = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    geo = models.OneToOneField(Geo, on_delete=models.CASCADE)

class Company(models.Model):
    name = models.CharField(max_length=100)
    
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    website = models.URLField(max_length=200)
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    username = models.CharField(max_length=100,null=True)


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id', db_column='userId')
    task = models.TextField(max_length=200)
    completed = models.BooleanField(default=False)



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    content = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, to_field='id', db_column='postId')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    text = models.TextField()

class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    title = models.TextField()

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos')
    title = models.TextField()
    url = models.URLField()
    thumbnailUrl = models.URLField()