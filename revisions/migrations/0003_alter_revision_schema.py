# Generated by Django 4.2 on 2023-05-01 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revisions', '0002_alter_revision_rev_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revision',
            name='schema',
            field=models.CharField(choices=[(1, 'день'), (2, 'ночь')]),
        ),
    ]
