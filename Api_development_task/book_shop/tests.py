from django.test import TestCase
import pytest
from django.urls import reverse
from django.test import Client

@pytest.mark.django_db
def test_get_request(client):
    response = client.get(reverse('book_shop:Book'))  
    assert response.status_code == 200
    assert 'Sucessfully worked' in str(response.content)

@pytest.mark.django_db
def test_post_request(client):
    response = client.post(reverse('book_shop:Book'), {
        "book_review":"Good book",
        "rating": 5,
        "book": 1
            })  
    assert response.status_code == 200
    assert 'Sucessfully worked' in str(response.content)
