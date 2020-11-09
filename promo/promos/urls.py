from django.urls import path

from .views import (
    PromoAPIListView,
    PromoAPIDetailView,
    PromoMeAPIView,
    UsePromoAPIView,
    PromoMeRemainingView,
    GetPromoView,
)

urlpatterns = [
    # admin endpoints
    path("", PromoAPIListView.as_view(), name="promo-list"),
    path("<int:pk>/", PromoAPIDetailView.as_view(), name="promo"),
    # noraml endpoints
    path("me/", PromoMeAPIView.as_view(), name="promo-me"),
    path("<int:pk>/use/", UsePromoAPIView.as_view(), name="use-promo"),
    path("<int:pk>/point/", PromoMeRemainingView.as_view(), name="remain-point"),
    path("<int:pk>/get/", GetPromoView.as_view(), name="get-promo"),
]