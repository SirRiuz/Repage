# Generated by Django 3.0.8 on 2021-03-06 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20210305_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='namespace',
            field=models.CharField(default='98bae92b822a4f02a3b0e18661042ca9', max_length=100),
        ),
    ]