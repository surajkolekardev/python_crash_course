from  django.db import models

class Employee(models.Model):
    """
    Models to store employee information.
    """
    name = models.CharField(max_length=100, help_text="Employee's full name")
    city = models.CharField(max_length=50, help_text="City")
    contact = models.CharField(max_length=15, help_text="Contact number")
    email = models.EmailField(help_text="Email Address")

    def __str__(self):
        return self.name