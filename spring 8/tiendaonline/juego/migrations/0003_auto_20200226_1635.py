# Generated by Django 2.2.10 on 2020-02-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0002_auto_20200225_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombreUsu',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
