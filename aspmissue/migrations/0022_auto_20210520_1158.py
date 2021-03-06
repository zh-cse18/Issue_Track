# Generated by Django 3.1.4 on 2021-05-20 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aspmissue', '0021_auto_20210520_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aftersalesanalysis',
            name='details',
        ),
        migrations.AddField(
            model_name='aftersalesanalysis',
            name='issue_or_improvement_details',
            field=models.TextField(blank=True, default='Example:Update the google patch.', null=True),
        ),
        migrations.AlterField(
            model_name='aftersalesanalysis',
            name='solved_or_improved',
            field=models.TextField(blank=True, default=' Example : Update the google patch – Not Fixed ( According to ASPM realease note ). Ø Change existing default wallpaper (add new wallpaper)- Fixed. Ø 3party wallpaper supported -Fixed Ø Lock and Unlock Icon change-Fixed', null=True),
        ),
        migrations.AlterField(
            model_name='aftersalesanalysis',
            name='type',
            field=models.CharField(choices=[('Improvement', 'Improvement'), ('Market Issue', 'Market Issue')], max_length=200),
        ),
    ]
