import uuid

from django.db import models


class TicketModel(models.Model):

    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4)
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    customer_uuid = models.UUIDField()
