# Generated by Django 3.2.21 on 2023-10-04 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_auto_20231004_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
    ]