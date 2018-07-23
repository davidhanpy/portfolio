from django.db import models

# Create your models here.
class Porfolio(models.Model):
  artist = models.CharField(max_length = 200, default = '')
  title = models.CharField(max_length = 256)
  thumbnail = models.FileField(upload_to = 'media')
  video = models.CharField(max_length = 512, default = '')
  uploadAt = models.DateTimeField(null = True, blank = True)

  def __str__(self):
    return self.artist + ' : ' + self.title

