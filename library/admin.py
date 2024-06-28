from django.contrib import admin
from library.models import User, Author, Book, IssuedBook
# Register your models here.

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(IssuedBook)