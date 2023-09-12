from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from .request_serializers import (
    WalletGetQuerySerializer,
    WalletCreateSerializer,
    TransactionGetQuerySerializer,
    TransactionCreateSerializer,
)
from .response_serializers import (
    WalletSerializer,
    TransactionSerializer,
)

from wallet.models import Wallet, Transaction


class OpenRequests:

    def get_permissions(self):
        return [AllowAny()]


class WalletView(OpenRequests, viewsets.ModelViewSet):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()
    authentication_classes = []
    
    @swagger_auto_schema(
        query_serializer=WalletGetQuerySerializer(),
        responses={
            200: WalletSerializer(many=True),
        },
    )
    def list(self, request, *args, **kwargs):
        input_serializer = WalletGetQuerySerializer(data=request.query_params)
        try:
            input_serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"message": "query is invalid"}, status=409)
        query_params = input_serializer.validated_data
        if query_params.get("sort"):
            self.queryset = self.queryset.order_by(query_params.get("sort"))
        if query_params.get("balance_from"):
            self.queryset = self.queryset.filter(
                balance__gte=query_params.get("balance_from")
            )
        if query_params.get("balance_to"):
            self.queryset = self.queryset.filter(
                balance__lte=query_params.get("balance_to")
            )
        return super().list(request)

    @swagger_auto_schema(
        request_body=WalletCreateSerializer(),
        responses={
            200: WalletSerializer(),
        },
    )
    def create(self, request, *args, **kwargs):
        input_serializer = WalletCreateSerializer(data=request.data)
        try:
            input_serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"message": "body is invalid"}, status=409)
        request_data = input_serializer.validated_data
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data)


class TransactionView(OpenRequests, viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    authentication_classes = []
    
    @swagger_auto_schema(
        query_serializer=TransactionGetQuerySerializer(),
        responses={
            200: TransactionSerializer(many=True),
        },
    )
    def list(self, request, *args, **kwargs):
        input_serializer = TransactionGetQuerySerializer(data=request.query_params)
        try:
            input_serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"message": "query is invalid"}, status=409)
        query_params = input_serializer.validated_data
        if query_params.get("sort"):
            self.queryset = self.queryset.order_by(query_params.get("sort"))
        if query_params.get("amount_from"):
            self.queryset = self.queryset.filter(
                balance__gte=query_params.get("amount_from")
            )
        if query_params.get("amount_to"):
            self.queryset = self.queryset.filter(
                balance__lte=query_params.get("amount_to")
            )
        return super().list(request)

    @swagger_auto_schema(
        request_body=TransactionCreateSerializer(),
        responses={
            200: TransactionSerializer(),
        },
    )
    def create(self, request, *args, **kwargs):
        input_serializer = TransactionCreateSerializer(data=request.data)
        try:
            input_serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"message": "body is invalid"}, status=409)
        request_data = input_serializer.validated_data
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        wallet = get_object_or_404(Wallet.objects.select_for_update(), pk=request_data.get("wallet_id"))
        self.perform_create(serializer)
        wallet.balance = wallet.balance + serializer.amount
        wallet.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data)
