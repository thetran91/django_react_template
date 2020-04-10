# Generated by Django 2.2.10 on 2020-04-10 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20200409_1508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='company_name',
            new_name='address',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mobile_phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='postcode',
            field=models.CharField(max_length=10, null=True),
        ),
    ]