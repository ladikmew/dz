from django.db import models


class Category(models.Model):
    name = models.CharField("Название", max_length=200)

    def __str__(self):
        return self.name


class Good(models.Model):
    category = models.ForeignKey("Category",
                                 on_delete=models.CASCADE
                                 )
    name = models.CharField("Наименование товара", max_length=200)
    description = models.TextField("Описание товара")
    price = models.FloatField("Цена")

    def __str__(self):
        return self.name
