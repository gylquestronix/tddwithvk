from rest_framework import serializers

from base.models import Rental, Reservation


class ReservationSerializer(serializers.ModelSerializer):
    rental = serializers.StringRelatedField()
    previous_reservation = serializers.IntegerField()

    class Meta:
        model = Reservation
        fields = ('__all__')
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['rental_name'] = representation['rental']

        del representation['rental']
        return representation
        
class RentalSerializer(serializers.ModelSerializer):
    # reservations = ReservationSerializer(many=True)
    class Meta:
        model = Rental
        # fields = ('id','name','reservations')
        fields = ('__all__')
        