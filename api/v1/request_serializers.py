from rest_framework import serializers


class WalletGetQuerySerializer(serializers.Serializer):
    limit = serializers.IntegerField(
        required=False,
        allow_null=True,
        default=10,
        label="amount of returning records",
    )
    offset = serializers.IntegerField(
        required=False,
        allow_null=True,
        default=0,
        label="amount of skipping records",
    )
    sort = serializers.ChoiceField(
        choices=(
            ("balance", "Balance ascending"),
            ("-balance", "Balance descending"),
        ),
        label="wallet sorting",
    )
    balance_from = serializers.IntegerField(
        required=False,
        allow_null=True,
        label="filter wallets with balance greater than",
    )
    balance_to = serializers.IntegerField(
        required=False,
        allow_null=True,
        label="filter wallets with balance smaller than",
    )


class WalletCreateSerializer(serializers.Serializer):
    label = serializers.CharField(
        max_length=255,
        required=True,
        allow_null=False,
        label="Name of new wallet",
    )


class TransactionGetQuerySerializer(serializers.Serializer):
    limit = serializers.IntegerField(
        required=False,
        allow_null=True,
        label="amount of returning records",
    )
    offset = serializers.IntegerField(
        required=False,
        allow_null=True,
        label="amount of skipping records",
    )
    sort = serializers.ChoiceField(
        choices=(
            ("amount", "Amount ascending"),
            ("-amount", "Amount descending"),
            ("updated_at", "Transaction date ascending"),
            ("-updated_at", "Transaction date descending"),
        ),
        label="transactions sorting",
    )
    amount_from = serializers.IntegerField(
        required=False,
        allow_null=True,
        label="filter transactions with amount greater than",
    )
    amount_to = serializers.IntegerField(
        required=False,
        allow_null=True,
        label="filter transactions with amount smaller than",
    )


class TransactionCreateSerializer(serializers.Serializer):
    txld = serializers.CharField(
        max_length=255,
        required=True,
        allow_null=False,
        label="Unique transaction token",
    )
    wallet_id = serializers.IntegerField(
        required=True,
        allow_null=False,
        label="Wallet pk",
    )
    amount = serializers.DecimalField(
        required=True,
        allow_null=False,
        max_digits=18,
        decimal_places=6,
        label="Transaction amount",
    )
