# Generated by Django 4.2.8 on 2024-01-31 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_storyprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storyprofile',
            old_name='uid',
            new_name='uids',
        ),
    ]