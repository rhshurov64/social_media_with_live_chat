# Generated by Django 3.2.19 on 2023-12-03 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0034_userloginhistory_duration_minutes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userloginhistory',
            name='logout_time',
            field=models.CharField(default='Currently Login', max_length=5000),
        ),
    ]
