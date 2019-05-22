from django.db import models


class Setup(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    term = models.CharField(max_length=50)
    limit = models.IntegerField()

    class Meta:
        ordering = ('created',)

class SelectedTweet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        ordering = ('created',)

class TrendingTopics(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        ordering = ('created',)

class Location(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()       
    longitude = models.FloatField()

    class Meta:
        ordering = ('created',)