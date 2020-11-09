import pytest

from promo.users.models import User
from promo.promos.models import Promo
from promo.users.tests.factories import UserFactory
from promo.promos.tests.factories import PromoFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def promo() -> Promo:
    return PromoFactory()
