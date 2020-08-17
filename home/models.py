from django.db import models
from django.conf import settings

# Create your models here.
class Home(models.Model):
  title = models.CharField(max_length=200)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
      self.published_date = timezone.now()
      self.save()

  def __str__(self):
      return self.title
