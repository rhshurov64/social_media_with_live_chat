# Generated by Django 3.2.19 on 2023-10-30 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20231030_0136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='liked_status',
        ),
        migrations.AddField(
            model_name='like',
            name='liked_status',
            field=models.BooleanField(default=False),
        ),
    ]
