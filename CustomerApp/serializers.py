from .models import Customer
from rest_framework import serializers


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','name','gender','account_type','balance','account_no','pub_date']