from stock.models import StockByDate, StockInfo, SourceInfo
from users.models import CustomUser
from .serializers import *
from stock.services import *
from rest_framework import generics, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .role import *
from django.http import JsonResponse


class StockByDateApiView(APIView):   

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        flag = StockByDateService.read_filtered(request.user, {"pk": pk})
        if len(flag) == 0:
            return JsonResponse({'status': 'false', 'message': "This record doesn't exist"},
                                status=400)
        stock = StockByDateService.read_by_pk(request.user, pk)
        return Response(StockByDateSerializer(stock).data)

    def delete(self, request, *args, **kwargs):
        role = get_role_json(request)
        if not role['is_specialist'] and not role['is_superuser']:
            return JsonResponse({'status':'false','message':'You do not have rights to get the information'}, status=403)
        pk = kwargs['pk']
        flag = StockByDateService.read_filtered(request.user, {"pk": pk})
        if len(flag) == 0:
            return JsonResponse({'status': 'false', 'message': "This record doesn't exist"},
                                status=400)
        stock = StockByDateService.delete_by_pk(request.user, pk)
        return JsonResponse({'status': 'Ok', 'message': 'You deleted stock by date'},
                            status=200)

    def patch(self, request, *args, **kwargs):
        role = get_role_json(request)
        if not role['is_specialist'] and not role['is_superuser']:
            return JsonResponse({'status':'false','message':'You do not have rights to get the information'}, status=403)
        pk = kwargs['pk']
        flag = StockByDateService.read_filtered(request.user, {"pk": pk})
        if len(flag) == 0:
            return JsonResponse({'status': 'false', 'message': "This record doesn't exist"},
                                status=400)
        flag.update_by_pk(request.user,pk, request.data)
        return JsonResponse({'status': 'Ok', 'message': 'You changed stock by date data'},
                            status=200)


class StockInfoApiView(APIView):   

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        flag = StockInfoService.read_filtered(request.user, {"pk": pk})
        if len(flag) == 0:
            return JsonResponse({'status': 'false', 'message': "This record doesn't exist"},
                                status=400)
        stock = StockInfoService.read_by_pk(request.user, pk)
        return Response(StockInfoSerializer(stock).data)

    def delete(self, request, *args, **kwargs):
        role = get_role_json(request)
        if not role['is_specialist'] and not role['is_superuser']:
            return JsonResponse({'status':'false','message':'You do not have rights to get the information'}, status=403)
        pk = kwargs['pk']
        flag = StockInfoService.read_filtered(request.user, {"pk": pk})
        if len(flag) == 0:
            return JsonResponse({'status': 'false', 'message': "This record doesn't exist"},
                                status=400)
        stock = StockInfoService.delete_by_pk(request.user, pk)
        return JsonResponse({'status': 'Ok', 'message': 'You deleted stock by date'},
                            status=200)

    def patch(self, request, *args, **kwargs):
        role = get_role_json(request)
        if not role['is_specialist'] and not role['is_superuser']:
            return JsonResponse({'status':'false','message':'You do not have rights to get the information'}, status=403)
        pk = kwargs['pk']
        flag = StockInfoService.read_filtered(request.user, {"pk": pk})
        if len(flag) == 0:
            return JsonResponse({'status': 'false', 'message': "This record doesn't exist"},
                                status=400)
        flag.update_by_pk(request.user,pk, request.data)
        return JsonResponse({'status': 'Ok', 'message': 'You changed stock by date data'},
                            status=200)


class SourceInfoApiView(APIView):   

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        flag = SourceInfoService.read_filtered(request.user, {"pk": pk})
        if len(flag) == 0:
            return JsonResponse({'status': 'false', 'message': "This record doesn't exist"},
                                status=400)
        stock = SourceInfoService.read_by_pk(request.user, pk)
        return Response(SourceInfoSerializer(stock).data)

    def delete(self, request, *args, **kwargs):
        role = get_role_json(request)
        if not role['is_specialist'] and not role['is_superuser']:
            return JsonResponse({'status':'false','message':'You do not have rights to get the information'}, status=403)
        pk = kwargs['pk']
        flag = SourceInfoService.read_filtered(request.user, {"pk": pk})
        if len(flag) == 0:
            return JsonResponse({'status': 'false', 'message': "This record doesn't exist"},
                                status=400)
        stock = SourceInfoService.delete_by_pk(request.user, pk)
        return JsonResponse({'status': 'Ok', 'message': 'You deleted stock by date'},
                            status=200)

    def patch(self, request, *args, **kwargs):
        role = get_role_json(request)
        if not role['is_specialist'] and not role['is_superuser']:
            return JsonResponse({'status':'false','message':'You do not have rights to get the information'}, status=403)
        pk = kwargs['pk']
        flag = SourceInfoService.read_filtered(request.user, {"pk": pk})
        if len(flag) == 0:
            return JsonResponse({'status': 'false', 'message': "This record doesn't exist"},
                                status=400)
        flag.update_by_pk(request.user,pk, request.data)
        return JsonResponse({'status': 'Ok', 'message': 'You changed stock by date data'},
                            status=200)


class CustomUserApiView(APIView):   

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        flag = CustomUserService.read_filtered(request.user, {"pk": pk})
        if len(flag) == 0:
            return JsonResponse({'status': 'false', 'message': "This record doesn't exist"},
                                status=400)
        stock = CustomUserService.read_by_pk(request.user, pk)
        return Response(CustomUserSerializer(stock).data)

    def delete(self, request, *args, **kwargs):
        role = get_role_json(request)
        if not role['is_specialist'] and not role['is_superuser']:
            return JsonResponse({'status':'false','message':'You do not have rights to get the information'}, status=403)
        pk = kwargs['pk']
        flag = CustomUserService.read_filtered(request.user, {"pk": pk})
        if len(flag) == 0:
            return JsonResponse({'status': 'false', 'message': "This record doesn't exist"},
                                status=400)
        stock = CustomUserService.delete_by_pk(request.user, pk)
        return JsonResponse({'status': 'Ok', 'message': 'You deleted stock by date'},
                            status=200)

    def patch(self, request, *args, **kwargs):
        role = get_role_json(request)
        if not role['is_specialist'] and not role['is_superuser']:
            return JsonResponse({'status':'false','message':'You do not have rights to get the information'}, status=403)
        pk = kwargs['pk']
        flag = CustomUserService.read_filtered(request.user, {"pk": pk})
        if len(flag) == 0:
            return JsonResponse({'status': 'false', 'message': "This record doesn't exist"},
                                status=400)
        flag.update_by_pk(request.user,pk, request.data)
        return JsonResponse({'status': 'Ok', 'message': 'You changed stock by date data'},
                            status=200)

#TODO REP pattern
class CreateUserApiView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = CreateUserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StockByDateCreateApiView(APIView):
    def post(self, request):
        serializer = StockByDateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StockInfoCreateApiView(APIView):
    def post(self, request):
        serializer = StockInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SourceInfoCreateApiView(APIView):
    def post(self, request):
        serializer = SourceInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)