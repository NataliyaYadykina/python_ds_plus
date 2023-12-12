import pytest
from ex06 import (Project, User,
                  LevelProjectException, AccessProjectException)


@pytest.fixture
def project():
    return Project('ex06_users.json')


@pytest.fixture
def new_user_valid():
    return User(level=3, id='15', name='Vladas')


@pytest.fixture
def new_user_error():
    return User(level=0, id='12345', name='Vladimir')


@pytest.fixture
def excisting_user():
    return User(level=1, id='1', name='Vlad')


@pytest.fixture
def not_excisting_user():
    return User(level=1, id='123123123', name='Nick')


def test_auth_correct(excisting_user: "User", project: "Project"):
    project.auth(excisting_user.name, excisting_user.id)
    assert project.admin == excisting_user


def test_incorrect_auth(not_excisting_user: "User", project: "Project"):
    with pytest.raises(AccessProjectException):
        project.auth(not_excisting_user.name, not_excisting_user.id)


def test_add_new_valid(excisting_user: "User",
                       new_user_valid: "User",
                       project: "Project"):
    project.auth(excisting_user.name, excisting_user.id)
    assert project.admin == excisting_user
    project.add_new_user(new_user_valid.name,
                         new_user_valid.id,
                         new_user_valid.level)
    assert excisting_user in project.users


def test_add_new_user_invalid(excisting_user: "User",
                              new_user_error: "User",
                              project: "Project"):
    project.auth(excisting_user.name, excisting_user.id)
    assert project.admin == excisting_user
    with pytest.raises(LevelProjectException):
        project.add_new_user(new_user_error.name,
                             new_user_error.id,
                             new_user_error.level)
