# Generated by Django 5.0.3 on 2024-03-09 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_file',
            field=models.FileField(default='NULL', upload_to='uploads/'),
        ),
    ]