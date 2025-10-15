from django.db import models

# Company Model
class Company(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=20, choices=(('IT', 'IT'), ('Non IT', 'Non IT')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# Employee model
class Employee(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    position = models.CharField(max_length=10, choices=(('manager', 'manager'), ('developer', 'developer'), ('hr', 'hr')))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)