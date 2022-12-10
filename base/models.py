from django.db import models


# Create your models here.
class Rental(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    rental = models.ForeignKey(Rental,related_name="reservations", on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()

    # class Meta:
    #     indexes = [
    #     models.Index(fields=['checkin']),
    # ]
    # indexing 


    def __str__(self):
        return 'Res-%s ID' %(self.id) 



'''
from base.models import Rental, Reservation
Rental.objects.create(name="Rental-1")
Rental.objects.create(name="Rental-2")
rentals = Rental.objects.all()

import datetime
  
# creating an instance of 
# datetime.date(1965, 1, 1)
d = datetime(2015, 10, 09, 23, 55, 59, 342380)
  
# creating an instance of 
# with foreignKey
# 
# 
Reservation.objects.create(rental = Rental.objects.get(id=1),checkin=datetime.date(2022,1,1),checkout=datetime.date(2022,1,13))
Reservation.objects.create(rental = Rental.objects.get(id=1),checkin=datetime.date(2022,1,20),checkout=datetime.date(2022,2,10))
Reservation.objects.create(rental = Rental.objects.get(id=1),checkin=datetime.date(2022,2,20),checkout=datetime.date(2022,3,10))
Reservation.objects.create(rental = Rental.objects.get(id=2),checkin=datetime.date(2022,1,2),checkout=datetime.date(2022,1,20))
Reservation.objects.create(rental = Rental.objects.get(id=2),checkin=datetime.date(2022,1,20),checkout=datetime.date(2022,2,11))



'''