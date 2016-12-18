from django.contrib import admin

from .models import Category, ContentManagerCategory
from article.models import Article

admin.site.register(Category)
admin.site.register(ContentManagerCategory)
admin.site.register(Article)
