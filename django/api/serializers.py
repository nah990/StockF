from rest_framework import serializers
from stock.models import StockByDate, StockInfo, SourceInfo

class StockByDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockByDate
        fields = ('ticket_id', 'min_price', 'avg_price', 'max_price',
         'forecast_date', 'created_at', 'updated_at',
          'outdated_status', 'final_accuracy')


class StockInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockInfo
        fields = ('name', 'ticket', 'source_id')


class SourceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceInfo
        fields = ('name', 'rating')