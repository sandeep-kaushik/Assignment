from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Expense(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    expense_amount=models.IntegerField(default=0)
    desciption=models.TextField(default='')
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user)










