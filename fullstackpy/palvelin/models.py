from django.db import models
#Djangon olio relaatio mallinnus = ORM
class Currency(models.Model):
    name = models.CharField(max_length=60)
    rate = models.FloatField()

    def _str_(self):
        return self.name