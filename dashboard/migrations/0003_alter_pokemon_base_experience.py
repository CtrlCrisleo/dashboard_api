# Generated by Django 4.0.4 on 2022-05-02 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_pokemon_delete_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='base_experience',
            field=models.IntegerField(),
        ),
    ]
