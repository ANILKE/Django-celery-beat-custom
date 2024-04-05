# Generated by Django 2.1.3 on 2024-04-05 07:16

from django.db import migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0012_periodictask_expire_seconds'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodictask',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(default='Europe/Istanbul', help_text='Timezone for setting default timezone.  Default is Europe/Istanbul.', verbose_name='Periodic Task Timezone'),
        ),
    ]
