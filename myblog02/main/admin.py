from django.contrib.auth.models import Group
from django.contrib import admin
from .models import BlogPost, BlogTag, Comment

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(BlogTag)
admin.site.register(Comment)

# Unregister your models here.
admin.site.unregister(Group)


