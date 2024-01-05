from django.db import models

class Artiles(models.Model):
    title = models.CharField('Название: ',max_length=25, default=None)
    anons = models.CharField('Анонс',max_length=250, default=None)
    full_text = models.TextField('Сатья', default=None)
    date = models.DateTimeField('Дата публикации', default=None)
    photo = models.CharField('Название фото:',max_length=25, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
