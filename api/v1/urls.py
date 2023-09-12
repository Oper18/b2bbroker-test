from django.urls import re_path

from .views import WalletView, TransactionView


urlpatterns = [
    re_path(r"wallet/$", WalletView.as_view({
        "get": "list",
        "put": "create",
    }), name="wallets"),
    re_path(r"transaction/$", TransactionView.as_view({
        "get": "list",
        "put": "create",
    }), name="transactions"),
]
