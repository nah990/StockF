from django.db import models
from django.db.models.deletion import SET_NULL
 
 
class SourceInfo(models.Model):
    name = models.TextField(null=True)
    rating = models.IntegerField(null=True)
 
 
class StockInfo(models.Model):
    name = models.TextField(null=True)
    ticket = models.TextField(max_length=5)
    source_id = models.ForeignKey(SourceInfo, related_name="source_info_id",
                                    on_delete=models.SET_NULL, null=True)
 
    def get_source_name(self):
        return self.source_id.name
 
    class Meta:
        ordering = ['ticket']
 
 
class StockByDate(models.Model):
    ticket_id = models.ForeignKey(StockInfo, related_name="stock_info_id",
                                    on_delete=models.SET_NULL, null=True)
    min_price = models.IntegerField(null=True)
    avg_price = models.IntegerField(null=True)
    max_price = models.IntegerField(null=True)
    forecast_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    outdated_status = models.BooleanField(default=False)
    final_accuracy = models.IntegerField(null=True)
 
    def get_ticket_name(self):
        return self.ticket_id.name
 
    class Meta:
        ordering = ['forecast_date']