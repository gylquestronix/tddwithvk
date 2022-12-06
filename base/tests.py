# from django.test import TestCase

# Create your tests here.

# from rest_framework.test import APITestCase

import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from base.models import Rental, Reservation
from api.serializers import RentalSerializer, ReservationSerializer

import datetime

class ReservationTestCase(APITestCase):

    def setUp(self):
        Rental.objects.create(name="Rental-1")
        Rental.objects.create(name="Rental-2")

        Reservation.objects.create(
            rental = Rental.objects.get(id=1),
            checkin=datetime.date(2022,1,1),
            checkout=datetime.date(2022,1,13)
        )

        Reservation.objects.create(
            rental = Rental.objects.get(id=1),
            checkin=datetime.date(2022,1,20),
            checkout=datetime.date(2022,2,10)
        )

        Reservation.objects.create(
            rental = Rental.objects.get(id=1),
            checkin=datetime.date(2022,2,20),
            checkout=datetime.date(2022,3,10)
        )

        Reservation.objects.create(
            rental = Rental.objects.get(id=2),
            checkin=datetime.date(2022,1,2),
            checkout=datetime.date(2022,1,20)
        )

        Reservation.objects.create(
            rental = Rental.objects.get(id=2),
            checkin=datetime.date(2022,1,20),
            checkout=datetime.date(2022,2,11)
        )

    def test_reservation1(self):
        _id = 1
        rental_name = 'Rental-1'
        checkin = '2022-01-01'
        checkout = '2022-01-13'
        prev_id = " - "

        url = reverse('reservation', kwargs={"id":_id})
        response = self.client.get(url)

        self.assertEqual(response.data['rental_name'], rental_name)
        self.assertEqual(response.data['id'], _id)
        self.assertEqual(response.data['checkin'], checkin)
        self.assertEqual(response.data['checkout'], checkout)
        self.assertEqual(response.data['previous_reservation'], prev_id)
        self.assertEqual(response.status_code, 200)

    def test_reservation2(self):
        _id = 2
        rental_name = 'Rental-1'
        checkin = '2022-01-20'
        checkout = '2022-02-10'
        prev_id = 1

        url = reverse('reservation', kwargs={"id":_id})
        response = self.client.get(url)

        self.assertEqual(response.data['rental_name'], rental_name)
        self.assertEqual(response.data['id'], _id)
        self.assertEqual(response.data['checkin'], checkin)
        self.assertEqual(response.data['checkout'], checkout)
        self.assertEqual(response.data['previous_reservation'], prev_id)
        self.assertEqual(response.status_code, 200)

    def test_reservation3(self):
        _id = 3
        rental_name = 'Rental-1'
        checkin = '2022-02-20'
        checkout = '2022-03-10'
        prev_id = 2

        url = reverse('reservation', kwargs={"id":_id})
        response = self.client.get(url)

        self.assertEqual(response.data['rental_name'], rental_name)
        self.assertEqual(response.data['id'], _id)
        self.assertEqual(response.data['checkin'], checkin)
        self.assertEqual(response.data['checkout'], checkout)
        self.assertEqual(response.data['previous_reservation'], prev_id)
        self.assertEqual(response.status_code, 200)

    def test_reservation4(self):
        _id = 4
        rental_name = 'Rental-2'
        checkin = '2022-01-02'
        checkout = '2022-01-20'
        prev_id = ' - '

        url = reverse('reservation', kwargs={"id":_id})
        response = self.client.get(url)

        self.assertEqual(response.data['rental_name'], rental_name)
        self.assertEqual(response.data['id'], _id)
        self.assertEqual(response.data['checkin'], checkin)
        self.assertEqual(response.data['checkout'], checkout)
        self.assertEqual(response.data['previous_reservation'], prev_id)
        self.assertEqual(response.status_code, 200)

    def test_reservation5(self):
        _id = 5
        rental_name = 'Rental-2'
        checkin = '2022-01-20'
        checkout = '2022-02-11'
        prev_id = 4

        url = reverse('reservation', kwargs={"id":_id})
        response = self.client.get(url)

        self.assertEqual(response.data['rental_name'], rental_name)
        self.assertEqual(response.data['id'], _id)
        self.assertEqual(response.data['checkin'], checkin)
        self.assertEqual(response.data['checkout'], checkout)
        self.assertEqual(response.data['previous_reservation'], prev_id)
        self.assertEqual(response.status_code, 200)


        


