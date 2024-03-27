from django.db import models

class MCA(models.Model):
    """This class creates the models of the members of county assemblies
    """
    name = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    party = models.CharField(max_length=100)

    class Meta:
        """
        overrides the default behaviour of pluralization
        """
        verbose_name = 'MCA'
        verbose_name_plural = 'MCAs'

    def __str__(self):
        """
        The string representation
        """
        return self.name + ' ' + self.ward
