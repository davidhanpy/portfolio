from django.contrib import admin

from . import models
# Register your models here.
# admin.site.register(models.Post)
# admin.site.register(models.PostLike)
class ScoreInline(admin.TabularInline):
  model = models.PostScore

class LikeInline(admin.TabularInline):
  model = models.PostLike

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
  inlines = [
    LikeInline,
    ScoreInline
  ]