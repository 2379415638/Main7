# Generated by Django 2.0 on 2018-01-05 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20180105_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='filename',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
