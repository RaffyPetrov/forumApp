# Generated by Django 5.1.1 on 2024-10-07 16:54

import forumApp.posts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(validators=[forumApp.posts.validators.BadLanguageValidator()]),
        ),
    ]
