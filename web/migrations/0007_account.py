# Generated by Django 4.2.9 on 2024-02-29 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('web', '0006_settings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_blocked', models.BooleanField(default=False, verbose_name='Статус блокировки')),
                ('time_unblock', models.DateTimeField(blank=True, verbose_name='Время разблокировки')),
            ],
        ),
    ]