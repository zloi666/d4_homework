from django.contrib import admin

from library.models import Book, Author, Publisher

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    fields = ('ISBN', 'publisher', 'title', 'description', 'year_release', 'author', 'price', 'copy_count')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass