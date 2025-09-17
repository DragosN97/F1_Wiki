import pytest
from f1.models import Driver
from django.contrib.auth import get_user_model

@pytest.fixture
def user(db):
    return get_user_model().objects.create_user(username='Dragos1', password='Tomato123!@#')

@pytest.fixture
def logged_in_client(client, user):
    client.login(username='Dragos1', password='Tomato123!@#')
    return client

def test_driver_creation(db, user):
    saved_driver  = Driver.objects.create(name='Valteri Botas', team='Mercedes', age=33, created_by=user )

    db_driver = Driver.objects.first()
    assert saved_driver.name == db_driver.name

@pytest.fixture
def driver_obj(user):
    driver1 = Driver(name="Prost", team="Ferrari", age=33, created_by=user)
    driver1.save()
    return driver1

def test_check_driver_name(driver_obj):
    assert driver_obj.name == "Prost"
    assert True

def test_check_driver_age(driver_obj):
    assert driver_obj.age == 33
    assert True

def test_check_driver_team(driver_obj):
    assert driver_obj.team == "Ferrari"
    assert True

def test_driver_created_by(driver_obj, user):
    assert driver_obj.created_by == user
    assert True

def test_driver_str(driver_obj):
    string = f'Name: {driver_obj.name} Team: {driver_obj.team} Age: {driver_obj.age}'
    assert str(driver_obj) == string

@pytest.mark.django_db
def test_delete_driver_confirmation_page(logged_in_client, driver_obj):
    url = 'drivers/{}/delete/'.format(driver_obj.pk)
    response = logged_in_client.get(url)
    assert response.status_code == 200
    assert "Are you sure you want to delete this driver?" in response.text






