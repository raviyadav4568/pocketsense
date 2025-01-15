import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from expenses.models import Expense, Payment, Concern, Profile
from datetime import datetime

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_register_user(api_client):
    response = api_client.post('/api/auth/users/', {
        'email': 'newuser@example.com',
        'username': 'newuser',
        'password': 'user_321'
    })

    assert response.status_code == 201
    assert response.data['username'] == 'newuser'