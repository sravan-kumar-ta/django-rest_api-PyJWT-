# Generated by Django 3.2.11 on 2022-01-07 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='phone_number',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
