# Generated by Django 4.1.7 on 2023-04-14 12:20

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0008_alter_recipe_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', tinymce.models.HTMLField(verbose_name='Aprašymas')),
            ],
            options={
                'verbose_name': 'Informacija',
                'verbose_name_plural': 'Informacija',
            },
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Aprašymas'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='directions',
            field=tinymce.models.HTMLField(verbose_name='Gaminimo eiga'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='notes',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Pastabos'),
        ),
    ]
