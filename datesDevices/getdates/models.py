from django.db import models

# Create your models here.
class SystemParamets(models.Model):
    number_plot = models.IntegerField(default= None)
    number_equipment = models.IntegerField(default= None)
    number_node = models.IntegerField(default= None)
    name = models.CharField(max_length=255)
    date_of_repair = models.IntegerField(default= None)
    replaced_parts = models.CharField(max_length=255)
    next_replacement_date = models.IntegerField(default= None)

    def __str__(self) -> str:
        return self.name
