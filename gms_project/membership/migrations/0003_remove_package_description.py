# Generated by Django 5.0.6 on 2024-06-30 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_remove_package_discription_package_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='description',
        ),
    ]
