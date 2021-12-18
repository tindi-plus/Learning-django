from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Make(models.Model):
    name = models.CharField(
        max_length=100,
        help_text='Auto make eg. Ford',
        validators=[RegexValidator(
            regex=r'^\w.{2,100}$', message='The Make must be more than 2 chars.')]
    )

    def __str__(self) -> str:
        """A string representation of a Make"""
        return self.name


class Auto(models.Model):
    auto_name = models.CharField(
        max_length=100,
        validators=[RegexValidator(
            regex=r'^\w.{2,100}$', message='Auto name must be greater than 2 chars.')]
    )
    make = models.ForeignKey('Make', on_delete=models.CASCADE, null=False)
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)

    def __str__(self) -> str:
        """A string representation of an Auto object"""
        return self.auto_name
