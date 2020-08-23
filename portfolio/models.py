from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=200)
  subtitle = models.CharField(max_length=200)
  start_date = models.DateTimeField(blank=True, null=True)
  end_date = models.DateTimeField(blank=True, null=True)
  text = models.TextField()
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
      self.published_date = timezone.now()
      self.save()

  def __str__(self):
      return self.title
