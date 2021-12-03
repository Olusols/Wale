from django.db import models
from Blog.models import Categories
from django.urls import reverse


class HomeSlider(models.Model):
    image = models.ImageField(upload_to='image/slider')


class Product(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post/', null=True)
    price = models.IntegerField()
    discount = models.IntegerField()
    slug = models.SlugField(max_length=255, default='my-product')

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.pk, self.slug])
