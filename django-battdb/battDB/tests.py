from django.test import TestCase
from . import models
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

# Create your tests here.

class HarvesterAPITest(APITestCase):
    def test_upload_dataset(self):
        """
        Ensure we can upload a dataset and have it parsed automatically
        """
        factory = APIRequestFactory()
        request = factory.put('/battDB/upload/', {'name': 'test dataset'}, format='json')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().name, 'foo')


def create_experiment(**kwargs) -> models.Experiment:
    exp = models.Experiment.objects.create(**kwargs)
    pass

