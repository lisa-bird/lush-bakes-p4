# Generated by Django 3.2.21 on 2023-09-29 18:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0004_rename_user_account_order_user_profile'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserAccount',
            new_name='UserProfile',
        ),
    ]