# Generated by Django 5.0 on 2023-12-24 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlite', '0003_alter_book_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='is_bestselling',
            field=models.BooleanField(default=False),
        ),
    ]