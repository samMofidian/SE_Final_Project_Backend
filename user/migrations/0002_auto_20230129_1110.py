# Generated by Django 3.2 on 2023-01-29 07:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_initial'),
        ('talent_survey', '0002_auto_20230129_1108'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoritecvs',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 1, 29, 7, 40, 2, 361977, tzinfo=utc), verbose_name='created time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='favoritecvs',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='updated time'),
        ),
        migrations.AddField(
            model_name='profile',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 1, 29, 7, 40, 5, 837227, tzinfo=utc), verbose_name='created time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='updated time'),
        ),
        migrations.RemoveField(
            model_name='favoritecvs',
            name='cv_id',
        ),
        migrations.AddField(
            model_name='favoritecvs',
            name='cv_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='favorite_cv', to='cv.cv'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='favoritecvs',
            name='user_id',
        ),
        migrations.AddField(
            model_name='favoritecvs',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='favorite_cv', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='UserSurvey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('result', models.URLField()),
                ('survey_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='talent_survey.talentsurvey')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surveys', to='user.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
