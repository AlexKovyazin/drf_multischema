from django.db import models


class Article(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'


class Balance(models.Model):
    shop = models.ForeignKey('Shop', models.CASCADE, blank=True, null=True)
    article = models.ForeignKey(Article, models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'balance'


class Shop(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop'

    def __repr__(self):
        return f'{self.code} - {self.name}'

    def __str__(self):
        return f'{self.code} - {self.name}'
