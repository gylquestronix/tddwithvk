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

@api_view(['GET'])
def getReservations(request):
    reservations = Reservation.objects.all()
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getReservation(request,id):
    reservation = Reservation.objects.get(pk=id)
    serializer = ReservationSerializer(reservation, many=False)
    return Response(serializer.data)

    # return Response({"rental_name":'Rental 1'})