# Generated by Django 3.2.19 on 2023-12-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0018_auto_20231210_0645'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='comment_notifcation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notification',
            name='like_notifcation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notification',
            name='post_id',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
    ]