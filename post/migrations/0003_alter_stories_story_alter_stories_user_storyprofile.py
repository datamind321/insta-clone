# Generated by Django 4.2.8 on 2024-01-31 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0002_stories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='story',
            field=models.FileField(upload_to='status'),
        ),
        migrations.AlterField(
            model_name='stories',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='StoryProfile',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
