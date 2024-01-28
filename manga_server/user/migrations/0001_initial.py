# Generated by Django 5.0.1 on 2024-01-26 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=31)),
                ('last_name', models.CharField(blank=True, max_length=31)),
                ('is_uploader', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
