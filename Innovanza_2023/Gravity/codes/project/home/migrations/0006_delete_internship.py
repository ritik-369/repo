# Generated by Django 4.1.7 on 2023-02-24 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_delete_interns_intern_duration_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Internship',
        ),
    ]