# Generated by Django 2.2.10 on 2020-04-09 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20191216_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='company_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
