# Generated by Django 3.2.9 on 2023-03-14 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('telegram_id', models.IntegerField(primary_key=True, serialize=False)),
                ('stupid_clicks', models.IntegerField(default=0)),
                ('fat_clicks', models.IntegerField(default=0)),
                ('dumb_clicks', models.IntegerField(default=0)),
            ],
        ),
    ]
