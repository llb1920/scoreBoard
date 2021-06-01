from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

# 分数表
class Score(models.Model):
    client = models.CharField(verbose_name='客户端号', max_length=16, unique=True)
    score = models.IntegerField(verbose_name='分数', default=0,
                                validators=[MaxValueValidator(10000000), MinValueValidator(1)])

    def __str__(self):
        return f'{self.client}'

    class Meta:
        verbose_name = '分数登记表'
        verbose_name_plural = verbose_name


# 名次表
class Rank(models.Model):
    c_id = models.OneToOneField(Score, on_delete=models.CASCADE, primary_key=True, )
    rank = models.IntegerField(verbose_name='名次', validators=[MinValueValidator(1)])
