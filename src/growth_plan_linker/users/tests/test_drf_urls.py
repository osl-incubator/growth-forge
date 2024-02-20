from django.urls import resolve, reverse

from growth_plan_linker.users.models import User


def test_user_detail(user: User) -> None:
    assert (
        reverse('api:user-detail', kwargs={'pk': user.pk})
        == f'/api/users/{user.pk}/'
    )
    assert resolve(f'/api/users/{user.pk}/').view_name == 'api:user-detail'


def test_user_list() -> None:
    assert reverse('api:user-list') == '/api/users/'
    assert resolve('/api/users/').view_name == 'api:user-list'


def test_user_me() -> None:
    assert reverse('api:user-me') == '/api/users/me/'
    assert resolve('/api/users/me/').view_name == 'api:user-me'
