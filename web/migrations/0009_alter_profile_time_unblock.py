# Generated by Django 4.2.9 on 2024-02-29 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_rename_account_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='time_unblock',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время разблокировки'),
        ),
    ]
