# Generated by Django 3.0.4 on 2020-04-23 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]