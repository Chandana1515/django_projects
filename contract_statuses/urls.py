from django.urls import path
from .views import ContractStatusListView, ContractStatusCreateView, ContractStatusUpdateView

app_name = 'contract_statuses'

urlpatterns = [
    path('', ContractStatusListView.as_view(), name='contract_status_list'),
    path('create/', ContractStatusCreateView.as_view(), name='contract_status_create'),
    path('update/<int:pk>/', ContractStatusUpdateView.as_view(), name='contract_status_update'),
]