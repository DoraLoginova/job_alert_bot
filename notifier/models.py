from django.db import models


class User(models.Model):
    telegram_id = models.CharField(max_length=50, unique=True)
    last_job_seen = models.CharField(max_length=200, blank=True)
