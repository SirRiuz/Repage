# Generated by Django 3.1.6 on 2021-03-04 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210216_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='namespace',
            field=models.CharField(default='f2a60b8ad9a642adacdeca5ea7788051', max_length=100),
        ),
    ]
