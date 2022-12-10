import timeit

from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Rental, Reservation

from .serializers import RentalSerializer


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
def getPerformance(request):
    return Response(timeit.timeit(stmt=getReservationsData, number=10000, globals=globals()))

def transformReservation(reservation):
    previous_reservation = reservation.previous_reservation

    if not previous_reservation:
        previous_reservation = ' - '
    
    return {
            'id': reservation.id, 
            'checkin': reservation.checkin.strftime("%Y-%m-%d"), 
            'checkout':reservation.checkout.strftime("%Y-%m-%d"),
            'rental_name': reservation.rental_name,
            'previous_reservation': previous_reservation,
        }

def getReservationsData():
    # reservations = Reservation.objects.annotate(
    #     previous_reservation=Subquery(Reservation.objects.filter(checkin__lt=OuterRef("checkin"), rental=OuterRef("rental_id")).order_by("-id").values('id')[:1]),
    #     rental_name=Subquery(Rental.objects.filter(pk=OuterRef("rental_id")).values('name')[:1])
    # )

    #ref:https://hakibenita.com/django-rest-framework-slow

    reservations = Reservation.objects.raw("SELECT base_reservation.id, base_reservation.checkin, base_reservation.checkout,(SELECT U0.id FROM base_reservation U0 WHERE (U0.checkin < base_reservation.checkin AND U0.rental_id = base_reservation.rental_id) ORDER BY U0.id DESC LIMIT 1) AS previous_reservation,(SELECT U0.name FROM base_rental U0 WHERE U0.id = base_reservation.rental_id LIMIT 1 ) AS rental_name FROM base_reservation")

    output = []

    for reservation in reservations:
        output.append(
            transformReservation(reservation)
        )

    return output

@api_view(['GET'])
def getReservations(request):
    data = getReservationsData()

    timer = timeit.timeit(stmt=getReservationsData, number=10000, globals=globals())

    print('timer')
    print(timer)
    
    return Response(data)


def getOneData():
    getReservationData(1)

def getReservationData(id):
    query = "SELECT base_reservation.id, base_reservation.checkin, base_reservation.checkout,(SELECT U0.id FROM base_reservation U0 WHERE (U0.checkin < base_reservation.checkin AND U0.rental_id = base_reservation.rental_id) ORDER BY U0.id DESC LIMIT 1) AS previous_reservation,(SELECT U0.name FROM base_rental U0 WHERE U0.id = base_reservation.rental_id LIMIT 1 ) AS rental_name FROM base_reservation WHERE id = {}".format(id)

    reservations = Reservation.objects.raw(query)

    for reservation in reservations:
        return transformReservation(reservation)

    return {}

@api_view(['GET'])
def getReservation(request,id):
    data = getReservationData(id)

    timer = timeit.timeit(stmt=getOneData, number=10000, globals=globals())

    print('timer')
    print(timer)

    return Response(data)