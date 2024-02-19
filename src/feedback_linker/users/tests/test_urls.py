from django.urls import resolve, reverse

from feedback_linker.users.models import User


def test_detail(user: User) -> None:
    assert (
        reverse('users:detail', kwargs={'pk': user.pk}) == f'/users/{user.pk}/'
    )
    assert resolve(f'/users/{user.pk}/').view_name == 'users:detail'


def test_update() -> None:
    assert reverse('users:update') == '/users/~update/'
    assert resolve('/users/~update/').view_name == 'users:update'


def test_redirect() -> None:
    assert reverse('users:redirect') == '/users/~redirect/'
    assert resolve('/users/~redirect/').view_name == 'users:redirect'
