# Generated by Django 3.2.19 on 2023-12-10 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0021_notification_replay_notifcation'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='comment_id',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
