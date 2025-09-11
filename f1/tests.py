import pytest
from f1.models import Driver
from django.contrib.auth import get_user_model

@pytest.fixture
def user(db):
    return get_user_model().objects.create_user(username='Dragos1', password='Tomato123!@#')

@pytest.fixture
def dogged_in_client(client, user):
    client.login(username='Dragos1', password='Tomato123!@#')
    return client

def test_driver_creation(db, user):
    saved_driver  = Driver.objects.create(name='Valteri Botas', team='Mercedes', age=33, created_by=user )

    db_driver = Driver.objects.first()
    assert saved_driver.title = db_driver.title


