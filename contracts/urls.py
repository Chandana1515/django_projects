from django.urls import path
from .views import ContractListView, ContractDetailView, ContractCreateView, ContractUpdateView, ContractDeleteView

app_name = 'contracts'

urlpatterns = [
    path('', ContractListView.as_view(), name='contract_list'),
    path('<int:pk>/', ContractDetailView.as_view(), name='contract_detail'),
    path('create/', ContractCreateView.as_view(), name='contract_create'),
    path('update/<int:pk>/', ContractUpdateView.as_view(), name='contract_update'),
    path('delete/<int:pk>/', ContractDeleteView.as_view(), name='contract_delete'),
]