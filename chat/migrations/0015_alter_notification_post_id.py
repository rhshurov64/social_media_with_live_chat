# Generated by Django 3.2.19 on 2023-12-10 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0014_alter_notification_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='post_id',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
    ]
