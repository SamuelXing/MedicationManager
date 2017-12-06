from django.db import models
from django.contrib.auth.models import User
from drugModule.models import Drug

# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User,null=True)
    drug = models.ForeignKey(Drug)

    OneTimePerDay = 'OneTime'
    TwoTimesPerDay = 'TwoTimes'
    ThreeTimesPerday = 'ThreeTimes'
    FREQUENCIES_CHOICES = (
        (OneTimePerDay, 'OneTimePerDay'),
        (TwoTimesPerDay, 'TwoTimesPerDay'),
        (ThreeTimesPerday, 'ThreeTimesPerDay'),
    )
    frequencies = models.CharField(max_length=15, choices=FREQUENCIES_CHOICES, default=TwoTimesPerDay)

    OnePillPerTime = 'One'
    TwoPillsPerTime = 'Two'
    ThreePillsPerTime = 'Three'
    DOSE_CHOICES = (
        (OnePillPerTime, 'OnePillPerTime'),
        (TwoPillsPerTime, 'TwoPillsPerTime'),
        (ThreePillsPerTime, 'TwoPillsPerTime'),
    )
    dose = models.CharField(max_length=5, choices=DOSE_CHOICES, default=ThreePillsPerTime)
    startDate = models.DateTimeField(auto_now_add=True)
    endDate = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
