# Generated by Django 3.1.5 on 2021-02-01 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='domestico',
            field=models.CharField(default='n/a', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animal',
            name='nome_animal',
            field=models.CharField(default='n/a', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animal',
            name='predador',
            field=models.CharField(default='n/a', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animal',
            name='venenoso',
            field=models.CharField(default='n/a', max_length=5),
            preserve_default=False,
        ),
    ]
