from django.contrib.auth.models import User
from django.db import models



class MealType(models.Model):
    name = models.CharField('Категория', max_length=100)
    image = models.ImageField('Изображение', upload_to='meal_types/')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'категории'


class Meal(models.Model):
    name = models.CharField('Название услуги', max_length=200)
    description = models.TextField('Описание услуги')
    price = models.CharField('Стоимость услуги', max_length=10)
    size = models.CharField('Стоимость услуги', max_length=10)
    meal_type = models.ForeignKey(MealType, on_delete=models.DO_NOTHING, verbose_name='Категория',
                                  related_name='meal_type')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'


class MealClick(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.DO_NOTHING)
    click_date = models.DateTimeField('Дата клика')
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
# class MealClick(models.Model):
#     meal = models.ForeignKey(Meal, on_delete=models.DO_NOTHING, related_name='MealClick')
#     user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user')
#     click_date = models.DateTimeField('Дата клика')
# class MealClick(models.Model):
#     meal = models.ForeignKey(Meal, on_delete=models.DO_NOTHING)
#     click_date = models.DateTimeField('Дата клика')
#     user = models.ForeignKey(User, default=13, on_delete=models.DO_NOTHING)


class ImageMeal(models.Model):
    image = models.ImageField('Изображение', upload_to='meal_images/')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


