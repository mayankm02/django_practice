from django.db import models

# Company Model
class Company(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=20, choices=(('IT', 'IT'), ('Non IT', 'Non IT')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

