from django.contrib import admin
from .models import Post, Categories, Review, Newsletter


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Categories, CategoryAdmin)
admin.site.register(Review)
admin.site.register(Newsletter)
