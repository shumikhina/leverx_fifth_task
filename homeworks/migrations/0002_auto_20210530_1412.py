# Generated by Django 3.2.3 on 2021-05-30 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readyhomework',
            name='comment',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='readyhomework',
            name='mark',
            field=models.IntegerField(null=True),
        ),
    ]
