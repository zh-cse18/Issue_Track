# Generated by Django 2.2 on 2020-12-29 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aspmissue', '0002_auto_20201229_1421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='software',
            old_name='model_sw',
            new_name='modelname',
        ),
    ]
