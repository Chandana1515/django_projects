from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView
from .models import ContractStatus
from .forms import ContractStatusForm
from django.urls import reverse_lazy

class ContractStatusListView(ListView):
    model = ContractStatus
    template_name = 'contract_statuses/contract_status_list.html'

class ContractStatusCreateView(CreateView):
    model = ContractStatus
    form_class = ContractStatusForm
    template_name = 'contract_statuses/contract_status_form.html'
    success_url = reverse_lazy('contract_statuses:contract_status_list')

class ContractStatusUpdateView(UpdateView):
    model = ContractStatus
    form_class = ContractStatusForm
    template_name = 'contract_statuses/contract_status_form.html'
    success_url = reverse_lazy('contract_statuses:contract_status_list')