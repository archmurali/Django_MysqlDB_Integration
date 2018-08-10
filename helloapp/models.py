# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class OcCart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    session_id = models.CharField(max_length=32)
    product_id = models.IntegerField()
    recurring_id = models.IntegerField()
    option = models.TextField()
    quantity = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        
        db_table = 'oc_cart'

    def __str__(self):
        return str(self.product_id)