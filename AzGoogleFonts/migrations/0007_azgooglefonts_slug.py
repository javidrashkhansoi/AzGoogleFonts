# Generated by Django 3.2.9 on 2021-11-08 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AzGoogleFonts', '0006_auto_20211109_0140'),
    ]

    operations = [
        migrations.AddField(
            model_name='azgooglefonts',
            name='slug',
            field=models.SlugField(default='mmm'),
        ),
    ]
