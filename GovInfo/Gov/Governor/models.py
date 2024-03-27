from django.db import models


class Governors(models.Model):
    """This class creates the models of governors       
    """
    name = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    party = models.CharField(max_length=100)

    class Meta:
        """
        overrides the default behaviour of pluralization
        """
        verbose_name = 'Governor'
        verbose_name_plural = 'Governors'

    def __str__(self):
        """
        The string representation of the class
        """
        return self.name + ' ' + self.county
