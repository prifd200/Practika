from rest_framework.response import Response
from rest_framework.views import APIView
from . import models,serializers
from  django.utils import timezone
import  json
class City(APIView):
    @staticmethod
    def get(request):
        try:
            serialized_data = serializers.Gorod(models.gorod.objects.all())
            return Response(serialized_data.data, status=200)
        except Exception:
            return Response(None, status=400)
class Street(APIView):
    @staticmethod
    def get(request, city_id):
        try:
            serialized_data = serializers.Street(models.ulica.objects.filter(id_City_id = city_id))
            return Response(serialized_data.data, status=200)
        except Exception:
            return Response(None, status=400)
class Shop(APIView):
    @staticmethod
    def get(request):
        try:
            city_id = request.GET.get('city') if request.GET.get('city') != '' else None
            street_id = request.GET.get('street') if request.GET.get('street') != '' else None
            open = request.GET.get('open') if request.GET.get('open') == '1' or request.GET.get('open') == '0' else None
            print(open)
            spisok = models.magaz.objects.all()
            if city_id is not None:
                spisok = spisok.filter(City=city_id)
            if street_id is not None:
                spisok = spisok.filter(Street=street_id)
            if open is not None:
                spisok = spisok.filter(Open__gte=timezone.now().time()) ^ spisok.filter(
                    Close__lte=timezone.now().time()) if open == '0' else spisok
                spisok = spisok.filter(Open__lte=timezone.now().time()) & spisok.filter(
                    Close__gte=timezone.now().time()) if open == '1' else spisok
            serialized_data = serializers.Magazin(spisok)
            return Response(serialized_data.data, status=200)
        except Exception:
            return Response(None, status=400)
    @staticmethod
    def post(request):
        try:
            data = request.data
            maga = models.magaz(
                Shop = data['Shop'],
                City = data['City'],
                Street = data['Street'],
                Building = data['Building'],
                Open = data['Open'],
                Close = data['Close'],
                id_City_id = data['id_City_id'],
                id_Street_id = data['id_Street_id']
            )

            maga.save()
            return Response(maga.id, status=200)
        except Exception :
            return Response(None, status=400)
class Magazini(APIView):
    @staticmethod
    def get(request, city_id,street_id,open):
        try:
            city_id = city_id if city_id != '' else None
            street_id = street_id if street_id != '' else None
            open = open if open != '' and open != '1' and open != '0' else None
            spisok = models.magaz.objects.all()
            if city_id is not None:
                spisok = spisok.filter(id_City_id = city_id)
            if street_id is not None:
                spisok = spisok.filter(id_Street_id = street_id)
            if open is not None:
                spisok = spisok.filter(Open__gte = timezone.now().time()) ^ spisok.filter(Close__lte = timezone.now().time()) if open == '0' else spisok
                spisok = spisok.filter(Open__lte=timezone.now().time()) & spisok.filter(Close__gte=timezone.now().time()) if open == '1' else spisok
            serialized_data = serializers.Magazin(spisok)
            return Response(serialized_data.data, status=200)
        except Exception:
            return Response(None, status=400)