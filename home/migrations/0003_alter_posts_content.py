# Generated by Django 4.0.5 on 2022-07-04 20:59

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_posts_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]