# Generated by Django 3.1.6 on 2021-03-04 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20210303_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='namespace',
            field=models.CharField(default='a280552713324c03baf9e7ee55d8a39e', max_length=100),
        ),
    ]
