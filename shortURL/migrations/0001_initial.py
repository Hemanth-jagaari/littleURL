# Generated by Django 3.2.9 on 2021-11-12 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLmap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.CharField(max_length=256)),
                ('short_url', models.CharField(max_length=16)),
            ],
        ),
    ]
