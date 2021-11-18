from django.urls import path, include


urlpatterns = [
    path('', include('stock.urls')),
    path('', include('frontend.urls')),
]
