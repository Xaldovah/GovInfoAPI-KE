"""The module includes implementation of the Gov model"""
from django.db import models
from django.core.validators import MinLengthValidator


class Gov(models.Model):
    """
    This is a class that reprsents all elected members
    """
    office = models.CharField(max_length=200)
    functions = models.CharField(
            max_length=500, validators=[MinLengthValidator(100)])
    salary = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        """
        overrides the default behaviour of the model pluralization
        """
        verbose_name = 'Gov'
        verbose_name_plural = 'Gov'

    def calculate_remaining_days(self):
        """
        Calculates the remaining days in office
        Returns None if end_date is null
        """
        if self.end_date is None:
            return None
        today = datetime.date.today()
        delta = self.end_date - today
        return delta.days

    @property
    def remaining_days(self):
        """
        Property to access the calculated remaining days
        """
        return self.calculate_remaining_days()
