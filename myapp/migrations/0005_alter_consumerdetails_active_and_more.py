# Generated by Django 4.0 on 2021-12-16 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_consumerdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumerdetails',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='consumerdetails',
            name='location',
            field=models.CharField(default='abc', max_length=100),
        ),
    ]
