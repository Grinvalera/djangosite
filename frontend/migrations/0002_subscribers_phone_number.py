# Generated by Django 2.2.7 on 2019-11-24 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribers',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]