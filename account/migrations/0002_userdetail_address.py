# Generated by Django 3.0.2 on 2020-01-31 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='address',
            field=models.TextField(default='d'),
            preserve_default=False,
        ),
    ]
