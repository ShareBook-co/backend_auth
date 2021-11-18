from django.db import models
from .user import User
from .grade import Grade
from .editorial import Editorial
from .author import Author

class Book(models.Model):

    id_book   = models.AutoField(primary_key=True)
    isbn      = models.IntegerField(default=0)
    user      = models.ForeignKey(User, related_name='book', on_delete=models.CASCADE)
    title     = models.CharField('Title', max_length = 256)
    language  = models.CharField('Language', max_length = 30)
    price     = models.IntegerField(default=0)
    state     = models.BooleanField(default=True)
    editorial = models.ForeignKey(Editorial, related_name='editorial', on_delete=models.CASCADE)
    author    = models.ManyToManyField(Author)
    grade     = models.ForeignKey(Grade, related_name='grade', on_delete=models.CASCADE)
