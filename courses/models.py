from django.db import models


NULLABLE = {'blank': True, 'null': True}

class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Курс')
    preview = models.ImageField(upload_to='image/', **NULLABLE, verbose_name='Превью')
    description = models.TextField(verbose_name='Содержание курса')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Урок')
    crss = models.ForeignKey('courses.Course', on_delete=models.SET_NULL, null=True, verbose_name='Урок курса')
    description = models.TextField(verbose_name='Содержание урока')
    preview = models.ImageField(upload_to='image/', **NULLABLE, verbose_name='Превью')
    video = models.URLField(**NULLABLE, verbose_name='Видео')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.name

