# Generated by Django 5.0.6 on 2024-07-04 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('calories', models.FloatField()),
                ('carbohydrates', models.FloatField()),
                ('cholesterol', models.FloatField()),
                ('fat_saturated', models.FloatField()),
                ('fat_total', models.FloatField()),
                ('fiber', models.FloatField()),
                ('potassium', models.FloatField()),
                ('protein', models.FloatField()),
                ('sodium', models.FloatField()),
                ('sugar', models.FloatField()),
            ],
        ),
    ]