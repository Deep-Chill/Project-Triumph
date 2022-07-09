from django.contrib import admin
from .models import Newspaper, Article, SocialPosts

admin.site.register(Newspaper)
admin.site.register(Article)
admin.site.register(SocialPosts)