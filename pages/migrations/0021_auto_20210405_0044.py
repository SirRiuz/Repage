# Generated by Django 2.2.12 on 2021-04-05 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_auto_20210319_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='namespace',
            field=models.CharField(default=True, max_length=500),
        ),
    ]