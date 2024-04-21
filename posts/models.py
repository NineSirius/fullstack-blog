from django.db import models

class Post(models.Model):
  content = models.TextField(blank=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  is_published = models.BooleanField(default=True)

