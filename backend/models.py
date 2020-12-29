from django.db import models


class CommonInfo(models.Model):
    # Flag to manage user active in the system
    is_deleted = models.BooleanField(default=False)
    # Track when user has been created
    created_at = models.DateTimeField(auto_now_add=True)
    # Track when user information get updated
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
