from rest_framework import serializers

from base.models import Rental, Reservation


class ReservationSerializer(serializers.ModelSerializer):
    # rental = serializers.StringRelatedField()
    # previous_reservation = serializers.IntegerField()

    class Meta:
        model = Reservation
        fields = ('__all__')

    def getPreviousRentalId(self, previous_reservation):
        if not previous_reservation:
            return ' - '
        else:
            return previous_reservation
            # return self.getResId(previous_reservation) for Res-1 ID
    
    def getResId(self, id):
        return 'Res-%s ID' %(id) 

    
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # representation['previous_reservation'] = self.getPreviousRentalId(representation['previous_reservation'])

        # representation['rental_name'] = representation['rental']

        # del representation['rental']
        return representation
        
class RentalSerializer(serializers.ModelSerializer):
    # reservations = ReservationSerializer(many=True)
    class Meta:
        model = Rental
        # fields = ('id','name','reservations')
        fields = ('__all__')
        