# Generated by Django 4.1.13 on 2024-06-09 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_category_author'),
        ('todo', '0006_alter_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category'),
        ),
    ]
