# Generated by Django 2.2.1 on 2019-05-13 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_setup'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tweet',
        ),
        migrations.RemoveField(
            model_name='selectedtweet',
            name='term',
        ),
        migrations.AddField(
            model_name='selectedtweet',
            name='ponctuation',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
