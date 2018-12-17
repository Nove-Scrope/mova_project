# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actor(models.Model):
    actorid = models.IntegerField(primary_key=True, blank=True, null=False)
    name = models.TextField(blank=True, null=True)
    filmid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Actor'


class Director(models.Model):
    directorid = models.IntegerField(primary_key=True, blank=True, null=False)
    name = models.TextField(blank=True, null=True)
    filmid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Director'


class Film(models.Model):
    filmid = models.IntegerField(primary_key=True, blank=True, null=False)
    name = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    score_rate = models.TextField(blank=True, null=True)
    score_num = models.TextField(blank=True, null=True)  # This field type is a guess.
    date = models.TextField(blank=True, null=True)
    boxoffice = models.TextField(blank=True, null=True)  # This field type is a guess.
    day_boxoffice = models.TextField(blank=True, null=True)  # This field type is a guess.
    week_boxoffice = models.TextField(blank=True, null=True)  # This field type is a guess.
    score = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Film'


class Type(models.Model):
    typeid = models.IntegerField(primary_key=True, blank=True, null=False)
    name = models.TextField(blank=True, null=True)
    filmid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Type'
