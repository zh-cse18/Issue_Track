# Generated by Django 3.1.4 on 2021-03-10 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aspmissue', '0013_auto_20210310_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuesummary',
            name='diff_two_version',
            field=models.IntegerField(blank=True, max_length=200, null=True),
        ),
    ]
