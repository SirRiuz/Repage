# Generated by Django 3.1.6 on 2021-03-04 21:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0013_auto_20210304_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='page',
            name='namespace',
            field=models.CharField(default='3e3dd540f6224026ad1a3a78299e3e5c', max_length=100),
        ),
    ]
