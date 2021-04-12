import os

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from . import models

# Create your tests here.


class HarvesterAPITest(APITestCase):
    def test_upload_dataset(self):
        """
        Ensure we can upload a dataset and have it parsed automatically
        """
        # TODO: Create a new token as part of the test, to avoid using a fixed one
        token = "52f1021a6e32e4202acab1c5c19f0067cc1ce38a"

        pathname = "media/biologic.csv"
        (dirname, filename) = os.path.split(pathname)
        url = "http://127.0.0.1:8000/battDB/upload/" + filename
        data = open(pathname, "rb")
        headers = {
            "Authorization": "Token " + token,
            "Content-Type": "application/octet-stream",
        }
        # factory = APIRequestFactory()
        # request = factory.put('/battDB/upload/%s' % filename, {'name': 'test dataset'}, format='json')
        # response = self.client.put(url, data=data, format='json')
        response = self.client.put(url, data=data, headers=headers, format="raw")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            models.ExperimentDataFile.objects.get().fhash,
            "7776fadaf51c99476d1d7228ff790fcc",
        )


def create_experiment(**kwargs) -> models.Experiment:
    exp = models.Experiment.objects.create(**kwargs)
    pass
