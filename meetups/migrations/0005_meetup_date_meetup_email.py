# Generated by Django 4.0 on 2021-12-24 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0004_participant_meetup_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateField(default='2021-12-08'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetup',
            name='email',
            field=models.EmailField(default='test@test.com', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
