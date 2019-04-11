# Create your models here.
from django.db import models
from django.urls import reverse


class Connection(models.Model):
    CONNECTION_TYPES = [('mysql+pymysql', 'mySQL'), ('oracle', 'Oracle')]

    usr_name = models.CharField(max_length=250)
    passwd = models.CharField(max_length=250, null=True, blank=True)
    server_addr = models.CharField(max_length=250)
    conn_type = models.CharField(
        max_length=50, choices=CONNECTION_TYPES)
    db_name = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('connection:index')

    def __str__(self):
        return self.db_name
