# Generated by Django 3.2.9 on 2021-11-08 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AzGoogleFonts', '0002_alter_azgooglefonts_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='azgooglefonts',
            name='designer',
        ),
        migrations.AddField(
            model_name='azgooglefonts',
            name='designer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AzGoogleFonts.fontdesigners'),
        ),
    ]
