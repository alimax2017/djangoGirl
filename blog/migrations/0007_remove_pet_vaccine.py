# Generated by Django 3.2 on 2021-05-05 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210505_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='vaccine',
        ),
    ]
