# Generated by Django 4.2.1 on 2023-05-18 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_bookmark_like_reply_alter_feed_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='like_count',
        ),
    ]