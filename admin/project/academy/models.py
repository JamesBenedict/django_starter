# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Invite(models.Model):
		name = models.CharField(max_length=500)
		branch = models.CharField(max_length=500)
		GENDER_CHOICES = (
			("M", "Male"),
			("F", "Female"),
			("N", "Non-binary"),
			("?", "Unknown")
		)
		gender = models.CharField(
			max_length=1,
			choices=GENDER_CHOICES,
			default="?"
		)
		data_of_birth = models.DateField(null=True, blank=True)
		RACE_CHOICES = (
			("A", "Asian"),
			("B", "Black"),
			("L", "Latino"),
			("W", "White"),
			("O", "Other"),
			("?", "Unknown")
		)
		RACE = models.CharField(
			max_length=10,
			choices=RACE_CHOICES,
			default="?"
		)
		notes = models.TextField(blank=True)