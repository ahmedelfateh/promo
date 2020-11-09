from datetime import datetime
from django.utils import timezone
from rest_framework import generics, mixins, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Promo
from promo.users.models import User
from .serializers import (
    PromosSerializer,
    PromosUseSerializer,
    PromoPointSerializer,
    GetPromoSerializer,
)

from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """
    Permition Checking on User type admin
    """

    def has_permission(self, request, view):
        return request.user.is_admin


class IsNormal(permissions.BasePermission):
    """
    Permition Checking on User type normal
    """

    def has_permission(self, request, view):
        return request.user.is_normal


class IsPromoOwner(permissions.BasePermission):
    """
    Permition Checking if the requested User own the requested promo code
    """

    def has_object_permission(self, request, view, obj):
        promo = Promo.objects.get(promo_code=obj)
        return request.user == promo.user


class PromoAPIListView(mixins.CreateModelMixin, generics.ListAPIView):
    """
    List all the available promo codes for the Admin users
    Create new promo codes
    """

    serializer_class = PromosSerializer
    queryset = Promo.objects.all()
    permission_classes = [IsAdmin, IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PromoAPIDetailView(
    generics.RetrieveAPIView,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    """
    Get Specific promo by 'id' all the available promo codes for the Admin users
    update / patch the promo code
    delete the promo code
    """

    serializer_class = PromosSerializer
    queryset = Promo.objects.all()

    permission_classes = [IsAdmin, IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PromoMeAPIView(generics.ListAPIView):
    """
    List the promo codes associated with the request user
    """

    serializer_class = PromosSerializer
    permission_classes = [IsNormal, IsAuthenticated]

    def get_queryset(self):
        return Promo.objects.filter(user=self.request.user)


class UsePromoAPIView(generics.GenericAPIView):
    """
    Allow user to get pointes from  promo
    """

    serializer_class = PromosUseSerializer
    queryset = Promo.objects.all()
    permission_classes = [IsPromoOwner, IsNormal, IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = self.get_object()
        promo = Promo.objects.get(promo_code=data)

        if promo.is_expired:
            raise ValidationError("This Promo has expired")

        if not promo.is_active:
            raise ValidationError("This Promo is not active any more")

        if int(request.data["used_amount"]) <= 0:
            raise ValidationError("Your Usage must be Grater than Zero")

        if promo.promo_amount < int(request.data["used_amount"]):
            raise ValidationError("Your Usage can't be Grater than Promo Amount")

        promo.promo_amount = promo.promo_amount - int(request.data["used_amount"])
        promo.save()

        return Response({"Remaning Amount": promo.promo_amount})


class PromoMeRemainingView(generics.RetrieveAPIView):
    """
    Get the remaining pointes from specific promo
    """

    serializer_class = PromoPointSerializer
    queryset = Promo.objects.all()
    permission_classes = [IsPromoOwner, IsNormal, IsAuthenticated]


class GetPromoView(generics.GenericAPIView, mixins.UpdateModelMixin):
    """
    Allow normal users to get promo codes
    """

    serializer_class = GetPromoSerializer
    queryset = Promo.objects.all()
    permission_classes = [IsNormal]

    def put(self, request, *args, **kwargs):
        data = self.get_object()
        promo = Promo.objects.get(promo_code=data)

        if promo.is_expired:
            raise ValidationError("This Promo has expired")

        if not promo.is_active:
            raise ValidationError("This Promo is not active any more")

        if promo.user:
            raise ValidationError("This Promo is Taken")

        user = User.objects.get(id=request.data["user"])

        if user.is_admin:
            raise ValidationError("Admin Users Can't have any Promos")

        return self.update(request, *args, **kwargs)