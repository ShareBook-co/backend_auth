from django.db import models

class Grade(models.Model):

    id_grade   = models.AutoField(primary_key=True)
    name_grade = models.CharField('Grade', max_length = 30)
