from django.urls import path
from django.views.generic import TemplateView

app_name = 'stock'

urlpatterns = [
    path('test', TemplateView.as_view(template_name="stock/index.html")),
    path('', TemplateView.as_view(template_name="stock/index.html")),
]