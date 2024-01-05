# Generated by Django 4.2.6 on 2023-11-27 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_artiles_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='artiles',
            name='photo',
            field=models.CharField(default=None, max_length=25, verbose_name='Название фото:'),
        ),
        migrations.AlterField(
            model_name='artiles',
            name='anons',
            field=models.CharField(default=None, max_length=250, verbose_name='Анонс'),
        ),
        migrations.AlterField(
            model_name='artiles',
            name='date',
            field=models.DateTimeField(default=None, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='artiles',
            name='full_text',
            field=models.TextField(default=None, verbose_name='Сатья'),
        ),
        migrations.AlterField(
            model_name='artiles',
            name='title',
            field=models.CharField(default=None, max_length=25, verbose_name='Название: '),
        ),
    ]