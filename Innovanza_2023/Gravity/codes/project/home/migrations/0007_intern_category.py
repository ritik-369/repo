# Generated by Django 4.1.7 on 2023-02-24 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_internship'),
    ]

    operations = [
        migrations.AddField(
            model_name='intern',
            name='category',
            field=models.CharField(default='', max_length=122),
        ),
    ]
