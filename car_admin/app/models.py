from django.db import models

MAX_LENGTH = 50


class Car(models.Model):
    brand = models.CharField(max_length=MAX_LENGTH)
    model = models.CharField(max_length=MAX_LENGTH)

    def __str__(self):
        return f'{self.brand} {self.model}'

    def review_count(self):
        return Review.objects.filter(car=self).count()


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Машина')
    title = models.CharField(max_length=100, verbose_name='Название обзора')
    text = models.TextField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.car) + ' ' + self.title


