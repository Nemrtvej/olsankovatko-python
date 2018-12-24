# Generated by Django 2.1.4 on 2018-12-24 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Sport name')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='sport',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reservations.Sport'),
            preserve_default=False,
        ),
    ]