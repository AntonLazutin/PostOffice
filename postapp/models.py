from django.db import models
from django.contrib.auth.models import User

CHOICES = (
    ("LT", "Letter"),
    ("PR", "Parcel"),
    ("NP", "Newspaper"),
)


class Employee(models.Model):
    pass


class Customer(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, related_name="customers", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)
    index = models.CharField(max_length=6)

    class Meta:
        db_table = 'customer'
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PostalItem(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, null=True)
    sender = models.ForeignKey(Customer, related_name='senders', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Customer, related_name='receivers', on_delete=models.CASCADE)
    departure_date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=9, choices=CHOICES)

    class Meta:
        db_table = 'postal_item'
        ordering = ['-departure_date']

    def __str__(self):
        return f"{self.get_type_display()} from {self.sender} to {self.receiver}" 
 