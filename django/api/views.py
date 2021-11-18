from stock.models import StockByDate, StockInfo, SourceInfo
from .serializers import StockByDateSerializer, StockInfoSerializer, SourceInfoSerializer
from rest_framework import generics


class StockByDateListCreate(generics.ListCreateAPIView):
    queryset = StockByDate.objects.all()
    serializer_class = StockByDateSerializer


class StockInfoListCreate(generics.ListCreateAPIView):
    queryset = StockInfo.objects.all()
    serializer_class = StockInfoSerializer


class SourceInfoListCreate(generics.ListCreateAPIView):
    queryset = SourceInfo.objects.all()
    serializer_class = SourceInfoSerializer