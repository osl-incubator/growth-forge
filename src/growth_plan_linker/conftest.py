import pytest

from growth_plan_linker.users.models import User
from growth_plan_linker.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def _media_storage(settings, tmpdir) -> None:  # type: ignore
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture()
def user(db) -> User:  # type: ignore
    return UserFactory()
