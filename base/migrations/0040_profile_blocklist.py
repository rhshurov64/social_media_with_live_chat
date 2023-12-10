# Generated by Django 3.2.19 on 2023-12-09 16:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0039_onlinestatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='blocklist',
            field=models.ManyToManyField(blank=True, related_name='blocklist', to=settings.AUTH_USER_MODEL),
        ),
    ]
