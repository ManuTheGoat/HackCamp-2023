# Generated by Django 4.2.7 on 2023-11-19 19:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('location', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('user', models.UUIDField(default=uuid.uuid4)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ListEntry',
            fields=[
                ('entry', models.UUIDField(default=uuid.uuid4)),
                ('id', models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=200)),
                ('entry', models.UUIDField(default=uuid.uuid4)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
