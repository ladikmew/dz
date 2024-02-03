from django.db import models


class Comment(models.Model):
    post = models.ForeignKey("blog.Post",
                             on_delete=models.CASCADE
                             )
    username = models.CharField("Ник", max_length=20)
    text = models.TextField("Текст")
    datetime = models.DateTimeField("Дата и время", auto_now_add=True)