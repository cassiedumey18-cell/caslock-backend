from rest_framework import serializers
from .models import Commission, Artwork, Price

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['currency', 'amount']

class ArtworkSerializer(serializers.ModelSerializer):
    prices = PriceSerializer(many=True, read_only=True)

    class Meta:
        model = Artwork
        fields = [
            'id',
            'title',
            'category',
            'size',
            'image',
            'description',
            'status',
            'prices',
        ]

class CommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commission
        fields = [
            'id',
            'name',
            'email',
            'whatsapp',
            'style',
            'size',
            'subjects',
            'description',
            'extra',
            'deadline',
            'priority',
            'status',
            'price',
            'created_at',
        ]