from django.contrib import admin
from .models import Category, Posts


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',  'add_date', 'add_time', 'url')
    search_fields = ('title', )
    list_per_page = 20


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'cat',  'post_author', 'post_time',
                    'post_date', 'url')
    list_filter = ('cat', )
    list_per_page = 20


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Posts, PostAdmin)
