from django.db import models


class Coordinate(models.Model):
    areacode = models.IntegerField(db_column='areaCode', primary_key=True)  # Field name made lowercase.
    area = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lot = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coordinate'


class Mountain1(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
    address_code = models.IntegerField(blank=True, null=True)
    lat = models.FloatField(db_column='LAT', blank=True, null=True)  # Field name made lowercase.
    lot = models.FloatField(db_column='LOT', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(blank=True, null=True)
    ht = models.FloatField(db_column='HT', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mountain1'


class Mountain2(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    stnid = models.TextField(blank=True, null=True)
    m_time = models.TextField(db_column='M_Time', blank=True, null=True)  # Field name made lowercase.
    m_level = models.TextField(db_column='M_level', blank=True, null=True)  # Field name made lowercase.
    m_reason = models.TextField(db_column='M_reason', blank=True, null=True)  # Field name made lowercase.
    m_view = models.TextField(db_column='M_view', blank=True, null=True)  # Field name made lowercase.
    m_detail = models.TextField(db_column='M_detail', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mountain2'


class Mountain3(models.Model):
    id = models.IntegerField(primary_key=True)
    areatreason = models.TextField(blank=True, null=True)
    areanm = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    etccourse = models.TextField(blank=True, null=True)
    mntheight = models.FloatField(blank=True, null=True)
    mntnm = models.TextField(blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    subnm = models.TextField(blank=True, null=True)
    tourisminf = models.TextField(blank=True, null=True)
    transport = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mountain3'



class LiveWeather(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    num = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    rainp = models.IntegerField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    hum = models.IntegerField(blank=True, null=True)
    wspd = models.FloatField(blank=True, null=True)
    di = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'live_weather'



class Bus(models.Model):
    id = models.IntegerField(primary_key=True)
    st_name = models.TextField(blank=True, null=True)
    addr = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lot = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus'


class Train(models.Model):
    id = models.IntegerField(primary_key=True)
    st_name = models.TextField(blank=True, null=True)
    addr = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lot = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'train'


class Subway(models.Model):
    id = models.IntegerField(primary_key=True)
    st_name = models.TextField(blank=True, null=True)
    lot = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subway'
