# Generated by Django 4.0.3 on 2023-07-13 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('place', models.CharField(max_length=20)),
                ('payment_date', models.DateTimeField()),
                ('meal_format', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=20)),
                ('degree_regret', models.IntegerField()),
            ],
        ),
    ]
