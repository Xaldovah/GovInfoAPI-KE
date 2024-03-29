# Generated by Django 5.0.3 on 2024-03-16 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemberOfParliament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField(null=True)),
                ('constituency', models.CharField(max_length=100)),
                ('county', models.CharField(max_length=100)),
                ('party', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('profile_image', models.URLField()),
            ],
        ),
    ]
