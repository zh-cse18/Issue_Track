# Generated by Django 3.1.4 on 2021-05-29 06:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aspmissue', '0025_auto_20210524_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pm_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='software',
            name='software_name',
        ),
        migrations.RemoveField(
            model_name='software',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='pmname',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='supplier_description',
        ),
        migrations.AlterField(
            model_name='aftersalesanalysis',
            name='feedback_date',
            field=models.DateField(default=datetime.date(2021, 5, 29)),
        ),
        migrations.AlterField(
            model_name='issuesummary',
            name='software',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aspmissue.software'),
        ),
        migrations.AddField(
            model_name='modelname',
            name='pm_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aspmissue.projectmanager'),
        ),
    ]
