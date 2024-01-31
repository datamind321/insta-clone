# Generated by Django 4.2.8 on 2024-01-31 10:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_stories_story_alter_stories_user_storyprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stories',
            name='id',
        ),
        migrations.AddField(
            model_name='stories',
            name='uid',
            field=models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='StoryProfile',
        ),
    ]