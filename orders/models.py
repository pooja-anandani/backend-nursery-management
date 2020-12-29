from django.db import models
from django.utils.translation import gettext as _
from backend.models import CommonInfo
from nursery.models import Plant
# Create your models here.
from django.contrib.auth import get_user_model

USER = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(
        USER, on_delete=models.CASCADE, related_name="cart_user")
    plant = models.ForeignKey(
        Plant, on_delete=models.CASCADE, related_name="cart_product")
    quantity = models.PositiveIntegerField(
        _("Quantity"), blank=False, null=False, default=1)
    
    class Meta:
        verbose_name="Cart"
        verbose_name_plural="Cart"


class Orders(CommonInfo, models.Model):

    user = models.ForeignKey(
        USER, on_delete=models.CASCADE, related_name="order_from")

    plant = models.ForeignKey(
        Plant, on_delete=models.CASCADE, related_name="ordered_product")
    nursery = models.ForeignKey(
        USER, on_delete=models.CASCADE, related_name="order_to")
    status = models.CharField(max_length=55)
    quantity = models.PositiveIntegerField(
        _("Quantity"), blank=False, null=False, default=1)
    total = models.DecimalField(
        _("Amount"), blank=False, null=False, decimal_places=2, max_digits=5)
    class Meta:
        verbose_name="Orders"
        verbose_name_plural="Orders"
