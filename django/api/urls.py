from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

schema_view = get_schema_view(
   openapi.Info(
      title="StockF API",
      default_version='v1',
      description="Simple web application for aggregating stock forecasts.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/',schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    #stock by date urls
    path('stocks/<int:pk>', views.StockByDateApiView.as_view(), name = 'stock'),
    path('stocks/', views.StockByDateCreateApiView.as_view(), name = 'stock'),
    #stock info urls
    path('stock-infos/<int:pk>', views.StockInfoApiView.as_view()),
    path('stock-infos/', views.StockInfoCreateApiView.as_view()),
    #source urls
    path('sources/<int:pk>', views.SourceInfoApiView.as_view()),
    path('sources/', views.SourceInfoCreateApiView.as_view()),
    #user urls
    path('users/<int:pk>', views.CustomUserApiView.as_view()),
    path('users', views.CreateUserApiView.as_view()),
]