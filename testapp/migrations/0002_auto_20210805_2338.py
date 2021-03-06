# Generated by Django 3.2.3 on 2021-08-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empmobnumbers',
            name='edegn',
            field=models.CharField(max_length=30, verbose_name='Designation'),
        ),
        migrations.AlterField(
            model_name='empmobnumbers',
            name='edept',
            field=models.CharField(choices=[('APSHCL', 'APSHCL'), ('PR', 'PR'), ('RWS', 'RWS')], default='apshcl', max_length=10, verbose_name='Name of the Department'),
        ),
        migrations.AlterField(
            model_name='empmobnumbers',
            name='emandal',
            field=models.CharField(max_length=20, verbose_name='Name of the Mandal'),
        ),
        migrations.AlterField(
            model_name='empmobnumbers',
            name='emn',
            field=models.IntegerField(verbose_name='Mobile Number'),
        ),
        migrations.AlterField(
            model_name='empmobnumbers',
            name='ename',
            field=models.CharField(max_length=30, verbose_name='name of the employee'),
        ),
    ]
