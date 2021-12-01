# Generated by Django 3.2.6 on 2021-09-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesandingredients', '0018_auto_20210927_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='caseQuantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='packSize',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='qtyUnits',
            field=models.CharField(choices=[('-- Weight --', (('Ounce (oz) (28.35 g)', 'Ounce (oz) (28.35 g)'), ('Pound (lb) (453.59 g)', 'Pound (lb) (453.59 g)'), ('Kilogram (Kg) (1000 g)', 'Kilogram (Kg) (1000 g)'), ('Tonne (T) (1000000 g)', 'Tonne (T) (1000000 g)'), ('Gram (g)', 'Gram (g)'))), ('-- Volume --', (('Pinch (pinch) (0.3 ml)', 'Pinch (pinch) (0.3 ml)'), ('US Teaspoon (tsp) (4.93 ml)', 'US Teaspoon (tsp) (4.93 ml)'), ('US Tablespoon (tbsp) (14.79 ml)', 'US Tablespoon (tbsp) (14.79 ml)'), ('Fluid-ounce (floz) (29.57 ml)', 'Fluid-ounce (floz) (29.57 ml)'), ('Deciliter (dL) (100 ml)', 'Deciliter (dL) (100 ml)'), ('US Cup (cup) (236.59 ml)', 'US Cup (cup) (236.59 ml)'), ('Pint (pt) (473.18 ml)', 'Pint (pt) (473.18 ml)'), ('Milliliter (ml)', 'Milliliter (ml)'), ('Quart (qt) (946.35 ml)', 'Quart (qt) (946.35 ml)'), ('Liter (L) (1000 ml)', 'Liter (L) (1000 ml)'), ('Gallon (gal) (3785.41 ml)', 'Gallon (gal) (3785.41 ml)'), ('Cubic Meter (kl) (1000000 ml)', 'Cubic Meter (kl) (1000000 ml)'), ('Each (each)', 'Each (each)'))), ('-- Quantity --', (('Dozen (dozen) (12 each)', 'Dozen (dozen) (12 each)'), ('Hundred (hundred) (100 each)', 'Hundred (hundred) (100 each)'), ('Thousand (thousand) (1000 each)', 'Thousand (thousand) (1000 each)'), ('Million (million) (1000000 each)', 'Million (million) (1000000 each)'))), ('-- Time --', (('Second (s)', 'Second (s)'), ('Minute (min) (60 s)', 'Minute (min) (60 s)'), ('Hour (hr) (3600 s)', 'Hour (hr) (3600 s)')))], default='', max_length=225),
            preserve_default=False,
        ),
    ]
