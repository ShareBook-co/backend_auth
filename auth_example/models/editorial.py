from django.db import models

class Editorial(models.Model):

    id_editorial   = models.AutoField(primary_key=True)
    name_editorial = models.CharField('Editorial', max_length = 30)