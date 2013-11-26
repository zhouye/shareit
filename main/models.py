from django.db import models

# Create your models here.

class User(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=20)
# Other fields

class Document(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=100)
#  user = models.ForeignKey(User)
  file = models.FileField(upload_to='documents/')
  score = models.IntegerField()
# Other fields
