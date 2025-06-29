# Generated by Django 5.0.7 on 2025-03-28 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=11, verbose_name='موبایل')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='ایمیل')),
                ('telegram', models.CharField(blank=True, max_length=100, null=True, verbose_name='تلگرام')),
                ('whatsapp', models.CharField(blank=True, max_length=100, null=True, verbose_name='واتساپ')),
                ('instagram', models.CharField(blank=True, max_length=100, null=True, verbose_name='اینستاگرام')),
            ],
            options={
                'verbose_name': 'شبکه',
                'verbose_name_plural': 'تماس با ما',
            },
        ),
    ]
