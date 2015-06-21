# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_update_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': 'Articulos', 'verbose_name': 'Articulo'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': 'Etiquetas', 'verbose_name': 'Etiqueta'},
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='titulo'),
        ),
    ]
