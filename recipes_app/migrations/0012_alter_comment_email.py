# Generated by Django 4.1.7 on 2023-04-16 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0011_alter_newsletter_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='El. paštas'),
        ),
    ]
