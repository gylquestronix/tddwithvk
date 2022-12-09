import timeit

from django.core.cache import cache
from django.db.models import OuterRef, Subquery
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Rental, Reservation

from .serializers import RentalSerializer, ReservationSerializer


@api_view(['GET'])
def getData(request):
    rentals = Rental.objects.all()
    serializer = RentalSerializer(rentals, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRentals(request):
    rentals = Rental.objects.all()
    serializer = RentalSerializer(rentals, many=True)
    return Response(serializer.data)


def getData():
    reservation_qs = Reservation.objects.filter(checkin__lt=OuterRef("checkin"),rental=OuterRef("rental_id"))

    reservations = Reservation.objects.all().annotate(
        previous_reservation=Subquery(reservation_qs.values('id')[:1])
    )
    serializer = ReservationSerializer(reservations, many=True)

    return serializer.data

@api_view(['GET'])
def getPerformance(request):

    return Response(timeit.timeit(stmt=getData, number=1000, globals=globals()))


@api_view(['GET'])
def getReservations(request):
    reservation_qs = Reservation.objects.filter(checkin__lt=OuterRef("checkin"),rental=OuterRef("rental_id"))

    reservations = Reservation.objects.all().annotate(
        previous_reservation=Subquery(reservation_qs.values('id')[:1])
    )
    serializer = ReservationSerializer(reservations, many=True)

    
    return Response(serializer.data)



@api_view(['GET'])
def getReservation(request,id):
    reservation_qs = Reservation.objects.filter(checkin__lt=OuterRef("checkin"),rental=OuterRef("rental_id")).order_by("-id")

    reservations = Reservation.objects.filter(id=id).annotate(
        previous_reservation=Subquery(reservation_qs.values('id')[:1])
    )

    # print('reservations')
    # print(reservations)
    
    if not reservations:
        return Response({})

    reservation = reservations[0]

    serializer = ReservationSerializer(reservation, many=False)

    return Response(serializer.data)