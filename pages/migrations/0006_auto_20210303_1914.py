# Generated by Django 3.1.6 on 2021-03-04 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20210303_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='namespace',
            field=models.CharField(default='11531d5065bb42d9b79b092f7b5b97a3', max_length=100),
        ),
    ]