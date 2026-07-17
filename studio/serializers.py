from rest_framework import serializers
from .models import Commission, Artwork

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = [
            'id',
            'title',
            'category',
            'size',
            'price_ngn',
            'price_usd',
            'image',
            'description',
            'status',
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