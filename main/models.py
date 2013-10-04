from django.db import models

# Create your models here.

from django.db import models

class User(models.Model):
  name = models.CharField(max_length=20)
# Other fields

class Document(models.Model):
  title = models.CharField(max_length=100)
  user = models.ForeignKey(User)
  filename =  models.CharField(max_length=100)
# Other fields
