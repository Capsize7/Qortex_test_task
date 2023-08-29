import pytest
from django.contrib.auth.models import User


def create_app_user(
        username='test',
        password=None,
        first_name="first name",
        last_name="last name",
        email="foo@bar.com",
        is_staff=False,
        is_superuser=False,
        is_active=True,
) -> User:
    user = User.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        email=email,
        is_staff=is_staff,
        is_superuser=is_superuser,
        is_active=is_active,
    )
    return user


@pytest.fixture
def admin(db):
    admin = create_app_user('admin', is_superuser=True)
    return admin


@pytest.fixture
def user(db):
    user = create_app_user('user', is_superuser=False)
    return user


def test_admin_and_user(admin, user):
    assert admin.is_superuser
    assert not user.is_superuser
    assert user.pk != admin.pk


