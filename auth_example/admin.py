from django.contrib import admin
from .models.user import User
from .models.book import Book
from .models.grade import Grade
from .models.editorial import Editorial
from .models.author import Author

# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Grade)
admin.site.register(Editorial)
admin.site.register(Author)
