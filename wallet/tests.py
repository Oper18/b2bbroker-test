from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from wallet.models import Wallet, Transaction


class WalletTests(APITestCase):
    def test_wallet_create(self):
        url = reverse("wallets")
        data = {"label": "wallet1"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Wallet.objects.count(), 1)
        self.assertEqual(Wallet.objects.get().label, 'wallet1')

    def test_wallets_list(self):
        url = reverse("wallets")
        query = {
            "limit": 10,
            "offset": 0,
            "sort": "balance",
            "balance_to": 10000,
            "balance_from": 100,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.results), 0)

    def test_transaction_create(self):
        url = reverse("transactions")
        data = {
            "txld": "test",
            "wallet_id": 1,
            "amount": 100,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Wallet.objects.count(), 1)
        self.assertEqual(Wallet.objects.get().balance, 100)
        data = {
            "txld": "test",
            "wallet_id": 1,
            "amount": 100,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 500)

    def test_transactions_lists(self):
        url = reverse("transactions")
        query = {
            "limit": 10,
            "offset": 0,
            "sort": "amount",
            "amount_to": 10000,
            "amount_from": 100,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.results), 1)
