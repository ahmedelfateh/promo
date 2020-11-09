from rest_framework import serializers

from .models import Promo
from promo.users.api.serializers import NewUserSerializer


class PromosSerializer(serializers.ModelSerializer):
    user = NewUserSerializer(read_only=True)

    class Meta:
        model = Promo

        fields = [
            "id",
            "user",
            "promo_type",
            "promo_code",
            "creation_time",
            "start_time",
            "end_time",
            "promo_amount",
            "is_active",
            "description",
        ]
        read_only_fields = [
            "id",
            "user",
        ]


class PromosUseSerializer(serializers.ModelSerializer):
    used_amount = serializers.IntegerField(write_only=True)

    class Meta:
        model = Promo

        fields = [
            "used_amount",
            "promo_amount",
        ]
        read_only_fields = [
            "promo_amount",
        ]


class PromoPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo

        fields = [
            "promo_amount",
        ]
        read_only_fields = [
            "promo_amount",
        ]


class GetPromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo

        fields = [
            "user",
        ]