# Generated by Django 4.0.5 on 2022-07-01 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('areacode', models.IntegerField(db_column='areaCode', primary_key=True, serialize=False)),
                ('area', models.TextField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lot', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'coordinate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mountain1',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='NAME', null=True)),
                ('address_code', models.IntegerField(blank=True, null=True)),
                ('lot', models.FloatField(blank=True, db_column='LOT', null=True)),
                ('lat', models.FloatField(blank=True, db_column='LAT', null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('ht', models.FloatField(blank=True, db_column='HT', null=True)),
                ('description', models.TextField(blank=True, db_column='DESCRIPTION', null=True)),
            ],
            options={
                'db_table': 'mountain1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mountain2',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('stnid', models.TextField(blank=True, null=True)),
                ('m_time', models.TextField(blank=True, db_column='M_Time', null=True)),
                ('m_level', models.TextField(blank=True, db_column='M_level', null=True)),
                ('m_reason', models.TextField(blank=True, db_column='M_reason', null=True)),
                ('m_view', models.TextField(blank=True, db_column='M_view', null=True)),
                ('m_detail', models.TextField(blank=True, db_column='M_detail', null=True)),
            ],
            options={
                'db_table': 'mountain2',
                'managed': False,
            },
        ),
    ]
