# Generated by Django 3.2 on 2023-06-28 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_consultant',
            field=models.BooleanField(default=False),
        ),
    ]