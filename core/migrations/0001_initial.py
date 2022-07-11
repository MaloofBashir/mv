# Generated by Django 4.0.4 on 2022-07-11 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=600)),
                ('Year', models.DateField()),
                ('imdbID', models.CharField(max_length=200)),
                ('Type', models.CharField(choices=[('Adventure', 'Adventure'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Horror', 'Horror'), ('Science fiction', 'Science fiction')], max_length=200)),
                ('Poster', models.CharField(max_length=1000)),
                ('Status', models.CharField(choices=[('private', 'private'), ('public', 'public')], max_length=100)),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.registration')),
            ],
        ),
    ]
