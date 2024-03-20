from django.db import models


class MemberOfParliament(models.Model):
    """This class creates the models of the member of parliament
    """
    name = models.CharField(max_length=100)
    constituency = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    party = models.CharField(max_length=100)


    class Meta:
        """
        overrides the default behaviour of pluralization
        """
        verbose_name = 'Member of Parliament'
        verbose_name_plural = 'Members of Parliament'

    def __str__(self):
        """
        The string representation
        """
        return self.name + ' ' + self.constituency
