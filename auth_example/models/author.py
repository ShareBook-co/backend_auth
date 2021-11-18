from django.db import models

class Author(models.Model):

    id_author   = models.AutoField(primary_key=True)
    name_author = models.CharField('Author', max_length = 30)