# Generated by Django 2.2 on 2020-12-29 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aspmissue', '0004_auto_20201229_1455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuesummary',
            old_name='new_issue_number',
            new_name='new_issue',
        ),
        migrations.RenameField(
            model_name='issuesummary',
            old_name='reopen_issue_number',
            new_name='reopen_issue',
        ),
        migrations.RenameField(
            model_name='issuesummary',
            old_name='issue_number_version_wise',
            new_name='total_issue',
        ),
    ]
