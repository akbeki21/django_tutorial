# Generated by Django 2.2.8 on 2020-12-24 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201222_2025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='text',
        ),
    ]
