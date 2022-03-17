from django.contrib import admin

# Register your models here.
from .models import Post, Comment

admin.site.reqister(Post)
admin.site.reqister(Comment)
