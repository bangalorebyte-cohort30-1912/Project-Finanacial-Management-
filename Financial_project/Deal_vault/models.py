from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

TYPE = (
    ('Income','income'),
    ('Expenses','Expenses')
)

METHOD = (
    ('Gpay','Gpay'),
    ('Phonepe','Phonepe'),
    ('paytm','paytm'),
    ('cash','cash'),
    ('debit','debit'),
    ('credit','credit')
)

class User(AbstractUser):
    pass

class Transactions(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    transaction_name = models.CharField(max_length=100)
    transaction_type= models.CharField("type_of_trans", max_length=60, choices=TYPE, default='Expense ')
    amount = models.IntegerField(default=0)
    Payment_method = models.CharField('method_of_pay',max_length=50,choices=METHOD, default='cash')

    # def __str__ (self):
    #     return f'{self.transaction_name}'
