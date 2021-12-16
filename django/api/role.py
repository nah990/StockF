from stock.services import CustomUserService
from .serializers import *

def get_role(request):
    is_user = False
    specialist = None
    is_specialist = False
    is_admin = False
    admin = None
    is_guest = True
    user = None

    if request.user.pk:
        user = CustomUserService.read_filtered(request.user, {'email': CustomUserService.read_by_pk(request.user, request.user.pk)})[0]
        if user.role == 0:
            is_user = True
            is_guest = False
        elif user.role == 1:
            is_specialist = True
            is_guest = False
        elif user.role == 2:
            is_admin = True
            is_guest = False

    return is_user, is_specialist,\
            is_admin, is_guest, \
            CustomUserSerializer(user).data

def get_role_json(request):
    is_user, is_specialist, is_admin, is_guest, user = get_role(request)
    return {'is_user': is_user, 'is_specialist': is_specialist, 
            'is_admin': is_admin, 'is_guest': is_guest, 'user': user}