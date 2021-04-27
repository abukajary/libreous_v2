from django.db import models
from main.models import Books
from Auth.models import AuthUser
# Create your models here.


class CartOrder(models.Model):
    product_id = models.BigIntegerField()
    book = models.ForeignKey(Books, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    total_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart_order'
