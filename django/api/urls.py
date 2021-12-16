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
    #stock by date urls
    path('stock/<int:pk>', views.StockByDateApiView.as_view(), name = 'stock'),
    path('stock/', views.StockByDateCreateApiView.as_view(), name = 'stock'),
    path('stock/list', views.StockByDateListCreate.as_view() , name = 'stock'),
    #stock info urls
    path('stock-info/<int:pk>', views.StockInfoApiView.as_view()),
    path('stock-info/list', views.StockInfoListCreate.as_view() ),
    #source urls
    path('source/<int:pk>', views.SourceInfoApiView.as_view()),
    path('source/list', views.SourceInfoListCreate.as_view() ),
    #user urls
    path('user/<int:pk>', views.CustomUserApiView.as_view()),
    path('user/list', views.CustomUserApiView.as_view()),
    path('user', views.CreateUserApiView.as_view()),
]