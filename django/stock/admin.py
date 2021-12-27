from django.contrib import admin
from .models import SourceInfo, StockInfo, StockByDate
# Register your models here.
admin.site.register(StockInfo)
admin.site.register(SourceInfo)
admin.site.register(StockByDate)