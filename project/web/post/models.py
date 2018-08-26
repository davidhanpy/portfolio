from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length = 256)
  body = models.TextField()
  image = models.FileField(upload_to='media',default='')

  def __str__(self):
    return self.title
  
  def __repr__(self):
        return str(self.to_dict())

  def to_dict(self):
      opts = self._meta
      data = {}
      for f in opts.concrete_fields + opts.many_to_many:
          if isinstance(f, models.ManyToManyField):
              if self.pk is None:
                  data[f.name] = []
              else:
                  data[f.name] = list(f.value_from_object(self).values_list('pk', flat=True))
          elif isinstance(f, models.DateTimeField):
              if f.value_from_object(self) is not None:
                  data[f.name] = f.value_from_object(self).timestamp()
              else:
                  data[f.name] = None
          elif isinstance(f, models.FileField):
              if f.value_from_object(self):
                  data[f.name] = f.value_from_object(self).url
              pass
          else:
              data[f.name] = f.value_from_object(self)
      return data


class PostLike(models.Model):
  post = models.ForeignKey(Post, on_delete = 'CASCADE')
  user = models.ForeignKey(User, on_delete = 'CASCADE')

  def __str__(self):
    return str(self.post.pk) + ' :: ' + self.user.username 

class PostScore(models.Model):
  post = models.ForeignKey(Post, on_delete = 'CASCADE')
  user = models.ForeignKey(User, on_delete = 'CASCADE')
  score = models.IntegerField()

  def __str__(self):
    return str(self.post.pk) + ' :: ' + self.user.username 