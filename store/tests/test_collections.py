from rest_framework.test import APIClient
from rest_framework import status
import pytest


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self):
        #Arrange -> Empty in this case

        #Act
        client = APIClient()
        response = client.post('/store/collections/', {
            'title': 'a'
        })

        #Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_if_user_is_admin_returns_403(self):
        #Arrange -> Empty in this case

        #Act
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post('/store/collections/', {
            'title': 'a'
        })

        #Assert
        assert response.status_code == status.HTTP_403_FORBIDDEN