from django.db import models


class UnemploymentRate19482010(models.Model):
    name = models.CharField(db_column='region_name', max_length=255)  # Field name made lowercase. Field renamed to r
    year = models.CharField(db_column='year', max_length=255)  # Field name made lowercase.
    value = models.CharField(db_column='value', max_length=255)  # Field name made lowercase.
    code = models.CharField(db_column='region_code', max_length=255)

    class Meta:
        managed = False
        ordering = ['year']
        db_table = 'salary'


class ErshouPrice(models.Model):
    coord = models.CharField(db_column='LOCATION', max_length=255)  # Field name made lowercase. Field renamed to r
    elevation = models.CharField(db_column='price', max_length=255)  # Field name made lowercase.
    typi = models.CharField(db_column='TYPE', max_length=255)

    class Meta:
        managed = False
        db_table = 'housedata'


class Province_GDP(models.Model):
    name = models.CharField(db_column='地区', max_length=255)  # Field name made lowercase. Field renamed to r
    value = models.CharField(db_column='2020年', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        ordering = ['value']
        db_table = 'province_gdp'


class City_GDP(models.Model):
    name = models.CharField(db_column='地区', max_length=255)  # Field name made lowercase. Field renamed to r
    value_2019 = models.CharField(db_column='2019', max_length=255)  # Field name made lowercase.
    value_2018 = models.CharField(db_column='2018', max_length=255)  # Field name made lowercase.
    value_2017 = models.CharField(db_column='2017', max_length=255)  # Field name made lowercase.
    value_2016 = models.CharField(db_column='2016', max_length=255)  # Field name made lowercase.
    value_2015 = models.CharField(db_column='2015', max_length=255)  # Field name made lowercase.
    value_2014 = models.CharField(db_column='2014', max_length=255)  # Field name made lowercase.
    value_2013 = models.CharField(db_column='2013', max_length=255)  # Field name made lowercase.
    value_2012 = models.CharField(db_column='2012', max_length=255)  # Field name made lowercase.
    value_2011 = models.CharField(db_column='2011', max_length=255)  # Field name made lowercase.
    value_2010 = models.CharField(db_column='2010', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        ordering = ['value_2019']
        db_table = 'city_gdp'


class City_Patents(models.Model):
    name = models.CharField(db_column='REGION', max_length=255)  # Field name made lowercase. Field renamed to r
    value_2019 = models.CharField(db_column='2019', max_length=255)  # Field name made lowercase.
    value_2018 = models.CharField(db_column='2018', max_length=255)  # Field name made lowercase.
    value_2017 = models.CharField(db_column='2017', max_length=255)  # Field name made lowercase.
    value_2016 = models.CharField(db_column='2016', max_length=255)  # Field name made lowercase.
    value_2015 = models.CharField(db_column='2015', max_length=255)  # Field name made lowercase.
    value_2014 = models.CharField(db_column='2014', max_length=255)  # Field name made lowercase.
    value_2013 = models.CharField(db_column='2013', max_length=255)  # Field name made lowercase.
    value_2012 = models.CharField(db_column='2012', max_length=255)  # Field name made lowercase.
    value_2011 = models.CharField(db_column='2011', max_length=255)  # Field name made lowercase.
    value_2010 = models.CharField(db_column='2010', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        ordering = ['value_2019']
        db_table = 'num_of_patents'


class Renthouseprice(models.Model):
    city2233 = models.CharField(db_column='City', max_length=255)
    Average = models.CharField(db_column='Average', max_length=255)

    class Meta:
        managed = False
        # ordering = ['Average']
        db_table = 'renthouseprice'


class Potential(models.Model):
    Name = models.CharField(db_column='Name', max_length=255)
    Value = models.CharField(db_column='Value', max_length=255)

    class Meta:
        managed = False
        # ordering = ['Ranks']
        db_table = 'city_development_potential'

class Five(models.Model):
    Name=models.CharField(db_column='Name', max_length=255)
    city_name=models.CharField(db_column='city', max_length=255)

    class Meta:
        managed = False
        db_table = 'top500_firms'

class Money(models.Model):
    Name=models.CharField(db_column='地区', max_length=255)
    Money=models.CharField(db_column='2020年', max_length=255)

    class Meta:
        managed = False
        db_table = 'money_to_use'