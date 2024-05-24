from django import forms
from .models import ContractStatus

class ContractStatusForm(forms.ModelForm):
    class Meta:
        model = ContractStatus
        fields = ['name', 'is_active']