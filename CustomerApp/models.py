from django.db import models
from django.db.models import Model
# Create your models here.
from django.utils import timezone
class Customer(models.Model):
    id = models.IntegerField(default=0,primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    account_type = models.CharField(max_length=10)
    balance = models.IntegerField(default=0)
    account_no = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published',default=timezone.now())

    def __str__(self):
        return "{0} , {1} , AccNo-{2} , Balance-{3}".format(self.name,self.gender,self.account_no,self.balance)