# Generated by Django 4.0.2 on 2022-05-18 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.TextField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]