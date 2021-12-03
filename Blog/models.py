from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category/')
    discount = models.IntegerField()
    date_added = models.DateTimeField(
        auto_now_add=True)
    slug = models.SlugField()

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', args=[self.pk, self.slug])


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    description = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post/')
    slug = models.SlugField(max_length=255)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[self.pk, self.slug])


class Comment(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    commment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('blog:comment-detail', args=[self.pk])


class Review(models.Model):
    fullname = models.CharField(max_length=255)
    image = models.ImageField(upload_to='review/')
    review = models.TextField()

    def get_absolute_url(self):
        return reverse('blog:review-detail', args=[self.pk])


class Newsletter(models.Model):
    email = models.EmailField()
