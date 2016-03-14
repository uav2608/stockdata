from django.db import models

# Create your models here.


class NasdaqList(models.Model):
#    class Meta:
#       db_table = "NasdaqList"
    symbol = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    last_sale = models.FloatField()
    market_cap = models.FloatField()
    ipo = models.IntegerField()
    sector = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    summary_quote = models.URLField()

    def __str__(self):
        return self.symbol