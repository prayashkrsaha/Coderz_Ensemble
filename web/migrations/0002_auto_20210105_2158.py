# Generated by Django 3.1.4 on 2021-01-05 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='name',
            field=models.TextField(),
        ),
    ]
