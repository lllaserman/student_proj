# Generated by Django 2.2.27 on 2022-05-27 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('notes', models.TextField(blank=True, verbose_name='Дополнительные записи')),
            ],
            options={
                'verbose_name': ('Группа',),
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=256, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, default='', max_length=256, verbose_name='Отчество')),
                ('birthday', models.DateField(null=True, verbose_name='Дата рождения')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото')),
                ('ticket', models.CharField(max_length=256, verbose_name='Билет')),
                ('notes', models.TextField(blank=True, verbose_name='Дополнительные заметки')),
                ('student_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='students.Group', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенти',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.Student', verbose_name='Староста'),
        ),
    ]
