from django.db import models

# Create your models here.
class Drug(models.Model):
    name = models.CharField(max_length=100, verbose_name="DrugName")
    description = models.CharField(max_length=500, verbose_name="DrugDescription", blank=True, null=True)
    toxicity = models.CharField(max_length=200, verbose_name="Toxicity", blank=True, null=True)
    interaction = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                    related_name='sides', related_query_name='sides')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


