# Generated by Django 5.0.3 on 2024-03-20 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parliament', '0002_alter_memberofparliament_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberofparliament',
            name='age',
        ),
        migrations.RemoveField(
            model_name='memberofparliament',
            name='email',
        ),
        migrations.RemoveField(
            model_name='memberofparliament',
            name='profile_image',
        ),
    ]