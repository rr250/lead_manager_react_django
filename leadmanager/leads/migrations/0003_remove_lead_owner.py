# Generated by Django 3.0.7 on 2020-06-16 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_lead_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='owner',
        ),
    ]