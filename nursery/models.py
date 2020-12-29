from django.db import models
import uuid
from backend.models import CommonInfo
from django.contrib.auth import get_user_model

# Create your models here.
USER = get_user_model()


class Plant(CommonInfo):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    image = models.ImageField(null=False, blank=False, upload_to='images/')
    price = models.DecimalField(max_digits=6, decimal_places=2,blank=False)
    name = models.CharField(max_length=256, blank=False)
    description = models.CharField(max_length=500, blank=True, default='')

    def __str__(self):
        return self.name