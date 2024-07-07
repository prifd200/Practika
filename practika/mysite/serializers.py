from  rest_framework import serializers
from . import  models
class Gorod(serializers.ModelSerializer):
    goroda = serializers.SerializerMethodField()

    class Meta:
        model = models.gorod
        fields = ['goroda',]

    @staticmethod
    def get_goroda(obj):
        try:
            return dict(id=obj.id,gorod=obj.City)
        except:
            return [dict(id=x.id,gorod=x.City) for x in obj]
class Street(serializers.ModelSerializer):
    street = serializers.SerializerMethodField()

    class Meta:
        model = models.ulica
        fields = ['street',]

    @staticmethod
    def get_street(obj):
        try:
            return dict(id=obj.id,gorod=obj.City,street=obj.Street)
        except:
            return [dict(id=x.id,gorod=x.City,street=x.Street) for x in obj]
class Magazin(serializers.ModelSerializer):
    magazin = serializers.SerializerMethodField()

    class Meta:
        model = models.magaz
        fields = ['magazin',]

    @staticmethod
    def get_magazin(obj):
        try:
            return dict(id=obj.id,shop = obj.Shop,gorod=obj.City,street=obj.Street)
        except:
            return [dict(id=x.id,shop=x.Shop,gorod=x.City,street=x.Street) for x in obj]