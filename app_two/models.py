from django.db import models


# Create your models here.
class Maker(models.Model):
    name = models.CharField(max_length=10)
    country = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class PModel(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.URLField(
        default='https://i.imgur.com/Ous4iGB.png')

    def __str__(self):
        return self.name


class Product(models.Model):
    pmodel = models.ForeignKey(PModel, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30, default='超級二手機')
    description = models.TextField(default='暫無說明')
    year = models.PositiveIntegerField(default=2016)
    price = models.IntegerField(default=-1)

    def __str__(self):
        return self.nickname


class PPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=20, default='手機照片')
    url = models.URLField(
        default='https://i.imgur.com/Z230eeq.png')

    def __str__(self):
        return self.description