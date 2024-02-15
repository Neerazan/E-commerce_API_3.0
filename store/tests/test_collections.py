from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework import status
import pytest



# we create inner function because if we pass collection create_collection(api_client, collection)
# pytest thinks "collection" also a fixture and search for it, and if not found it throws error
# so inner function is required in this case
@pytest.fixture
def create_collection(api_client:APIClient):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection


@pytest.mark.django_db    #This decorator helps to access the database
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self, api_client:APIClient, create_collection):
        #Arrange -> Empty in this case

        #Act
        response = create_collection({'title': 'a'})
        # response = api_client.post('/store/collections/', {
        #     'title': 'a'
        # })

        #Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_if_user_is_not_admin_returns_403(self, api_client:APIClient, authenticate, create_collection):
        #Arrange -> Empty in this case

        #Act
        authenticate()
        response = create_collection({'title': 'a'})

        #Assert
        assert response.status_code == status.HTTP_403_FORBIDDEN



    def test_if_data_is_invalid_returns_400(self, api_client:APIClient, authenticate, create_collection):
        #Arrange -> Empty in this case

        #Act
        authenticate(is_staff=True)
        response = create_collection({'title': ''})

        #Assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None
    

    def test_if_data_is_valid_returns_400(self, api_client:APIClient, authenticate, create_collection):
        #Arrange -> Empty in this case

        #Act
        authenticate(is_staff=True)
        response = create_collection({'title': 'a'})

        #Assert
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0