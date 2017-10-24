from django.db import models

class Search(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    user_id = models.CharField(max_length=64)
    tweet = models.CharField(max_length=4096, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search'

class Tweets(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    tweet = models.CharField(max_length=4096, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tweets'

class Users(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    screen_name = models.CharField(max_length=256, blank=True, null=True)
    followers_count = models.IntegerField(blank=True, null=True)
    friends_count = models.IntegerField(blank=True, null=True)
    statuses_count = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=2048, blank=True, null=True)
    url = models.CharField(max_length=256, blank=True, null=True)
    nit = models.IntegerField(blank=True, null=True)
    search = models.IntegerField(blank=True, null=True)
    tweet = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
