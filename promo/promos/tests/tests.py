import pytest
from promo.promos.models import Promo
from django.test import RequestFactory
from promo.promos.views import PromoAPIListView
from rest_framework.test import APIClient


pytestmark = pytest.mark.django_db


class TestPromo:
    def setUp(self):
        self.client = APIClient()
        print(self.client, "self.client")

    def test_get_queryset(self, promo: Promo, rf: RequestFactory):
        view = PromoAPIListView()
        request = rf.get("/fake-url/")
        request.promo = promo

        view.request = request

        assert promo in view.get_queryset()
