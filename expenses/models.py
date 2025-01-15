from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.user.username} Profile'

class Expense(models.Model):
    name = models.CharField(max_length=50) 
    description = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    split_details = models.JSONField()
    pending_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} - {self.total_amount}"

class Payment(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='payments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    payer = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_on = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment of {self.amount} by {self.user.username}'

class Concern(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='concerns')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='concerns')
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Concern by {self.user.username} on {self.date}'
