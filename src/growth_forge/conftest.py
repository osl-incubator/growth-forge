import pytest

from growth_forge.users.models import User
from growth_forge.users.tests.factories import UserFactory
from growth_forge.utils import ignore_vulture_issue


@pytest.fixture(autouse=True)
def _media_storage(settings, tmpdir) -> None:  # type: ignore
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture()
def user(db) -> User:  # type: ignore
    ignore_vulture_issue(db)
    return UserFactory()
