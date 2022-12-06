from rest_framework import serializers

from base.models import Rental, Reservation


class ReservationSerializer(serializers.ModelSerializer):
    rental = serializers.StringRelatedField()

    class Meta:
        model = Reservation
        fields = ('id', 'checkin', 'checkout', 'rental', 'rental_id')

    def getPreviousRentalId(self, representation):
        rental_id = representation['rental_id']
        current_id = representation['id']

        reservation = Reservation.objects.values().filter(rental=rental_id, id__lt=current_id).order_by("-id")[:1];

        if not reservation:
            return ' - '
        else:
            return reservation[0]['id']
            # return self.getResId(reservation[0]['id'])
    
    def getResId(self, id):
        return 'Res-%s ID' %(id) 

    
    def to_representation(self, instance):
        representation = super(ReservationSerializer,self).to_representation(instance)

        representation['previous_reservation'] = self.getPreviousRentalId(representation)

        representation['rental_name'] = representation['rental']

        del representation['rental']
        del representation['rental_id']
        # representation['ID'] = self.getResId(representation['id'])

        return representation
        
class RentalSerializer(serializers.ModelSerializer):
    # reservations = ReservationSerializer(many=True)
    class Meta:
        model = Rental
        # fields = ('id','name','reservations')
        fields = ('__all__')
        