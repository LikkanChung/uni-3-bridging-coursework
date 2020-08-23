from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
  type = models.CharField(max_length=200)
  detail = models.CharField(max_length=200)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
      self.published_date = timezone.now()
      self.save()

  def __str__(self):
      return self.detail

class Education(models.Model):
  name = models.CharField(max_length=200)
  school = models.CharField(max_length=200)
  location = models.CharField(max_length=200)
  start_date = models.DateTimeField(blank=True, null=True)
  end_date = models.DateTimeField(blank=True, null=True)
  text = models.TextField()
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
      self.published_date = timezone.now()
      self.save()

  def __str__(self):
      return self.name

class Experience(models.Model):
  role = models.CharField(max_length=200)
  location = models.CharField(max_length=200)
  start_date = models.DateTimeField(blank=True, null=True)
  end_date = models.DateTimeField(blank=True, null=True)
  text = models.TextField()
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
      self.published_date = timezone.now()
      self.save()

  def __str__(self):
      return self.role

class Volunteering(models.Model):
  role = models.CharField(max_length=200)
  location = models.CharField(max_length=200)
  start_date = models.DateTimeField(blank=True, null=True)
  end_date = models.DateTimeField(blank=True, null=True)
  text = models.TextField()
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
      self.published_date = timezone.now()
      self.save()

  def __str__(self):
      return self.role
