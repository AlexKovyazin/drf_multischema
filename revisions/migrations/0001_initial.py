# Generated by Django 4.2 on 2023-05-01 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base_models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rev_date', models.DateTimeField()),
                ('schema', models.CharField(choices=[('день', 1), ('ночь', 2)])),
                ('status', models.IntegerField()),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='revisions', to='base_models.shop')),
            ],
        ),
    ]
