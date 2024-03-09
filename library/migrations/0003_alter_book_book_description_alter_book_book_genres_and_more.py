# Generated by Django 5.0.3 on 2024-03-09 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_book_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_genres',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_isbn',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_isbn13',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_pages',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_publication_date',
            field=models.DateTimeField(blank=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_publisher',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_rating',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_total_ratings',
            field=models.IntegerField(blank=True),
        ),
    ]
