# Generated by Django 3.2.19 on 2023-10-25 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_modelone_modeltwo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelone',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='modelone',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
