from django.contrib import admin
# Из модуля models импортируем модель Post
from .models import Post

admin.site.register(Post) 