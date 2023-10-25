# Generated by Django 3.2.19 on 2023-10-30 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0015_auto_20231030_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='liked_status',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
