# Generated by Django 4.0.1 on 2022-01-15 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moinschwein', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accusation',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, verbose_name='timestamp'),
        ),
    ]