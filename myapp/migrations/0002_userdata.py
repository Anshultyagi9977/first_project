# Generated by Django 4.0 on 2021-12-14 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('address2', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=6)),
            ],
        ),
    ]
