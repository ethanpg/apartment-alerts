from django.db import models


class Applicant(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=255, blank=True)
    bedrooms = models.PositiveSmallIntegerField(null=True)
    income = models.PositiveIntegerField(null=True)

    def __str__(self):
        return "(%s) %s %s" % (self.id, self.name, self.phone_number)


class Property(models.Model):
    # this is the Twilio SMS number
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=1024)
    # this is the normal human contact number
    contact_phone = models.CharField(max_length=15)

    applicants = models.ManyToManyField(Applicant, blank=True)

    def __str__(self):
        return "(%s) %s: %s applicants" %\
            (self.id, self.phone_number, self.applicants.count())

    class Meta:
        verbose_name_plural = "Properties"


