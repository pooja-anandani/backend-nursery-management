# Generated by Django 3.1.4 on 2020-12-28 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='total',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5, verbose_name='Amount'),
            preserve_default=False,
        ),
    ]
