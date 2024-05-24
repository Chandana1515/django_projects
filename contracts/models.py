from django.db import models
from contract_statuses.models import ContractStatus

class Contract(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.ForeignKey(ContractStatus, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title