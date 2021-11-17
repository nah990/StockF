from django.urls import path
from . import views

urlpatterns = [
    path('api/stock/', views.StockByDateListCreate.as_view() ),
    path('api/stock-info/', views.StockInfoListCreate.as_view() ),
    path('api/source/', views.SourceInfoListCreate.as_view() ),
]