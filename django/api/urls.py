from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('stock/', views.StockByDateListCreate.as_view() ),
    path('stock-info/', views.StockInfoListCreate.as_view() ),
    path('source/', views.SourceInfoListCreate.as_view() ),
]