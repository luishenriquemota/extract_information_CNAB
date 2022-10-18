from pyexpat import model
from django.db import models
from django.forms import IntegerField
import uuid

from traitlets import default


class Transactions(models.Model):
    store_owner = models.CharField(max_length=15)
    store_name = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    hour = models.TimeField()
    date =  models.DateField()
    
    type = models.ForeignKey(
        "types_transactions.Types",on_delete=models.CASCADE, related_name="transactions"
    )


class Files(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    file = models.FileField(upload_to='uploads/')

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="files"
    )

