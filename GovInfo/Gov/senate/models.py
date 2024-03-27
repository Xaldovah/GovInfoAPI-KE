from django.db import models


class Senators(models.Model):
    """This class creates the models of the member of the senate
    """
    name = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    party = models.CharField(max_length=100)

    class Meta:
        """
        overrides the default behaviour of pluralization        
        """
        verbose_name = 'Senator'
        verbose_name_plural = 'Senators'

    def __str__(self):
        """
        The string representation
        """
        return self.name + ' ' + self.county
