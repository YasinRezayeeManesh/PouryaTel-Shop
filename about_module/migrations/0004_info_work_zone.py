# Generated by Django 5.0.7 on 2025-03-30 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_module', '0003_info_address_info_site_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='work_zone',
            field=models.CharField(default='', max_length=100, verbose_name='ساعت کاری'),
        ),
    ]
