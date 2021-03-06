# Generated by Django 2.2.10 on 2020-02-26 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0003_auto_20200226_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=50, null=True)),
                ('precioProducto', models.IntegerField(default=10, null=True)),
                ('cantidad', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='carrito1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='juego.Carrito'),
        ),
    ]
