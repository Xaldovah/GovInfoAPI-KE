# Generated by Django 5.0.3 on 2024-03-16 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parliament', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='memberofparliament',
            options={'verbose_name': 'Member of Parliament', 'verbose_name_plural': 'Members of Parliament'},
        ),
    ]
