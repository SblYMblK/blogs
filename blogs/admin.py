from django.contrib import admin
from .models import Post

admin.site.register(Post)
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author']
    search_fields = ['title']
    list_select_related = ['author']