# Generated by Django 4.2.1 on 2023-06-27 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_branch_article_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
