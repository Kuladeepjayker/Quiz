# Generated by Django 3.0.6 on 2020-12-05 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Questionsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('option_one', models.CharField(max_length=100)),
                ('option_two', models.CharField(max_length=100)),
                ('option_three', models.CharField(max_length=100)),
                ('option_four', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Questionsapp.Course')),
            ],
        ),
        migrations.DeleteModel(
            name='Questionsapp',
        ),
    ]