# Generated by Django 4.0.1 on 2022-02-05 15:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0002_alter_news_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='User',
            field=models.CharField(default=django.utils.timezone.now, max_length=20, verbose_name='Автор'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='date_pub',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
    ]