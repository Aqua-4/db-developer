# Generated by Django 2.1.5 on 2019-04-06 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='passwd',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
