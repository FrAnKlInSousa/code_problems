import pytest
import factory

from src.code_problems.code_wars.kyu_4.codewars_style_ranking_system import User, UserAlternative


class UserFactory(factory.Factory):
    class Meta:
        model = User

    User.rank = -8
    User.progress = 0

    @classmethod
    def _create(cls, model_class, **kwargs):
        user = model_class()

        for key, value in kwargs.items():
            setattr(user, key, value)
        return user

class UserFactoryAlternative(factory.Factory):
    class Meta:
        model = UserAlternative

    UserAlternative.total2 = 0

@pytest.fixture
def make_user():
    def _make_user(**kwargs):
        user = UserFactory(**kwargs)
        return user
    return _make_user


@pytest.fixture
def make_user_alternative():

    def _make_user(**kwargs):
        return UserFactoryAlternative(**kwargs)
    return _make_user