# Generated by Django 2.2 on 2019-05-08 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserDetails', '0014_remove_user_external_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='association',
            name='has_min_exception',
            field=models.BooleanField(default=False, help_text='If checked, this association has an exception to the minimum balance'),
        ),
        migrations.AlterField(
            model_name='association',
            name='is_choosable',
            field=models.BooleanField(default=True, help_text='If checked, this association can be chosen as membership by users'),
        ),
    ]
