from django.db import models


class Applicant(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return "(%s) %s" % (self.id, self.phone_number)

class Property(models.Model):
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=1024)

    applicants = models.ManyToManyField(Applicant, blank=True)

    def __str__(self):
        return "(%s) %s: %s applicants" %\
            (self.id, self.phone_number, self.applicants.count())

    class Meta:
        verbose_name_plural = "Properties"


