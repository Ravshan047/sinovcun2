# Generated by Django 5.2.3 on 2025-06-25 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_alter_policenotice_mahalla_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthcare',
            name='mahalla',
            field=models.ManyToManyField(related_name='healthcare_mahalla', to='news.mahalla'),
        ),
        migrations.AlterField(
            model_name='healthcare',
            name='village',
            field=models.ManyToManyField(related_name='healthcare_village', to='news.village'),
        ),
    ]
