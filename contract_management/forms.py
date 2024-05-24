from django import forms
from contracts.models import Contract
from contract_statuses.models import ContractStatus

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['title', 'description', 'status']
    
    def __init__(self, *args, **kwargs):
        super(ContractForm, self).__init__(*args, **kwargs)
        self.fields['status'].queryset = ContractStatus.objects.filter(is_active=True)