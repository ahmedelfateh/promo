import factory
import factory.fuzzy


from promo.users.tests.factories import UserFactory
from promo.promos.models import Promo


class ShipmentFactory(factory.django.DjangoModelFactory):
    promo_type = "CV"
    promo_code = "2134"
    creation_time = "2020-11-07"
    start_time = "2020-11-07"
    end_time = "2020-11-30"
    promo_amount = 13
    is_active = True
    description = "new promo"
    user = factory.SubFactory("UserFactory")

    class Meta:
        model = Promo
