# Generated by Django 3.1 on 2020-08-24 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.CharField(blank=True, max_length=8000, null=True),
        ),
    ]
