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
    path("", PromoAPIListView.as_view()),
    path("<int:id>/", PromoAPIDetailView.as_view()),
    # noraml endpoints
    path("me/", PromoMeAPIView.as_view()),
    path("<int:id>/use/", UsePromoAPIView.as_view()),
    path("<int:id>/point/", PromoMeRemainingView.as_view()),
    path("<int:id>/get/", GetPromoView.as_view()),
]