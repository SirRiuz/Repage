# Generated by Django 3.0.8 on 2021-03-06 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20210305_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='namespace',
            field=models.CharField(default='fd29e7430ad84c6d82113d129314fe1b', max_length=100),
        ),
    ]
