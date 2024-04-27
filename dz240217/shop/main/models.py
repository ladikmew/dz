from django.db import models


class Category(models.Model):
    name = models.CharField("Название", max_length=200)

    def __str__(self):
        return self.name 

def good_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / good_<id>/<filename>
    return 'good_{0}/{1}'.format(instance.id, filename)


class Good(models.Model):
    category = models.ForeignKey("Category",
                                 on_delete=models.CASCADE
                                 )
    name = models.CharField("Наименование товара", max_length=200)
    description = models.TextField("Описание товара")
    price = models.FloatField("Цена")
    img = models.ImageField(upload_to=good_directory_path)

    def __str__(self):
        return self.name
