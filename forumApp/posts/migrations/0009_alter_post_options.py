# Generated by Django 5.1.1 on 2024-11-05 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_post_approved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': [('can_approve_post', 'Can approve post')]},
        ),
    ]
