from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models import Sum

# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateField( auto_now_add=True)

    class Meta:
        abstract=True