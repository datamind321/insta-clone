# Generated by Django 4.2.8 on 2024-01-31 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_storyprofile_stories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storyprofile',
            old_name='user',
            new_name='username',
        ),
    ]