from django import forms
from djongo import models


class SkuItem(models.Model):
    id = models.IntegerField('规格id')
    name = models.CharField('规格名称', max_length=100)

    class Meta:
        abstract = True


class Skus(models.Model):
    id = models.IntegerField('规格id')
    name = models.CharField('规格名称', max_length=100)
    items = models.ArrayField(model_container=SkuItem)

    class Meta:
        abstract = True


class SpuInfo(models.Model):
    _id = models.CharField(max_length=10000)
    name = models.CharField('商品名', max_length=100)
    amount = models.FloatField('商品金额', max_length=99999)
    mainUrl = models.CharField('商品主图', max_length=10000)
    imgurls = models.JSONField('规格图', null=True, blank=True)
    sku = models.ArrayField(model_container=Skus)
    goodsList = models.JSONField(null=True, blank=True, default=[])

    objects = models.DjongoManager()
