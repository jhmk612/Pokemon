from django.contrib import admin
from .models import Post
from .forms import PostForm

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    form=PostForm


admin.site.register(Post, PostAdmin)