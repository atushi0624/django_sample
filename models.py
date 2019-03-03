from django.db import models

# Create your models here.

class company_ID(models.Model):
    name = models.CharField('出版社', max_length=255)

class App01(models.Model):
	title = models.CharField(max_length=140, verbose_name='タイトル')
	content = models.CharField(max_length=140, verbose_name='本文')
	company_ID = models.ForeignKey(company_ID, verbose_name="出版社",on_delete=models.CASCADE,)
	posted_date = models.DateTimeField(auto_now_add=True)
