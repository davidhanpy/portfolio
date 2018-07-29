from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length = 256)
  body = models.TextField()

  def __str__(self):
    return self.title

class PostLike(models.Model):
  post = models.ForeignKey(Post, on_delete = 'CASCADE')
  user = models.ForeignKey(User, on_delete = 'CASCADE')

  def __str__(self):
    return str(self.post.pk) + ' :: ' + self.user.username 