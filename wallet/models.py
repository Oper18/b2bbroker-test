from django.db import models


class Wallet(models.Model):
    label = models.CharField(
        verbose_name="Wallet name",
        max_length=255,
        unique=True,
    )
    balance = models.DecimalField(
        verbose_name="Transactions sum",
        max_digits=19,
        decimal_places=6,
        default=0.0,
    )
    created_at = models.DateTimeField(
        verbose_name="created date", auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="updated date", auto_now=True
    )

    def __str__(self) -> str:
        return f"{self.id} - {self.label}"


class Transaction(models.Model):
    wallet = models.ForeignKey(
        "wallet.Wallet",
        verbose_name="Wallet",
        on_delete=models.CASCADE,
        related_name="transactions",
    )
    txld = models.CharField(
        verbose_name="Unique required field",
        max_length=255,
        unique=True,
    )
    amount = models.DecimalField(
        verbose_name="Transactions sum",
        max_digits=18,
        decimal_places=6,
    )
    created_at = models.DateTimeField(
        verbose_name="created date", auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="updated date", auto_now=True
    )

    def __str__(self) -> str:
        return f"{self.wallet} - {self.amount}"
