# Generated by Django 4.2.9 on 2024-02-29 16:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0007_account'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Account',
            new_name='Profile',
        ),
    ]