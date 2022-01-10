from django.test import TestCase
from .models import CustomUser, CustomUserManager
from stock.db_manager import DBConfigManager
from stock.repositories import CustomUserRepository
from stock.services import CustomService, CustomUserService
from core.dataBuilder import *
from unittest.mock import MagicMock, Mock

class TestDBRoleConnection(TestCase):

    databases = '__all__'
    db_config_manager = DBConfigManager()

    @staticmethod
    def test_admin_connection():
        client_user = AdminUser().user
        assert(TestDBRoleConnection.db_config_manager.get_connection(client_user) == 'admin_role_connect')

    @staticmethod
    def test_superuser_connection():
        client_user = SuperUser().user
        assert(TestDBRoleConnection.db_config_manager.get_connection(client_user) == 'admin_role_connect')

    @staticmethod
    def test_user_connection():
        client_user = User().user
        assert(TestDBRoleConnection.db_config_manager.get_connection(client_user) == 'user_role_connect')

    @staticmethod
    def test_specialist_connection():
        client_user = SpecialistUser().user
        assert(TestDBRoleConnection.db_config_manager.get_connection(client_user) == 'specialist_role_connect')

    
class TestCustomUserRepository(TestCase):

    client_user = CustomUser(role=CustomUser.DEFAULT)

    @staticmethod
    def test_custom_user_repository_dependency_with_model():
        mock = MagicMock()
        CustomUserRepository.create(TestCustomUserRepository.client_user, mock)
        mock.save.assert_called_with(using=CustomUserRepository.db_config_manager.get_connection(TestCustomUserRepository.client_user))

    @staticmethod
    def test_admin_CRUD():
        user = AdminUser().user

        CustomUserRepository.create(TestCustomUserRepository.client_user, user)


        db_user = CustomUserRepository.read_by_pk(TestCustomUserRepository.client_user, 1)

        assert(db_user.id == 1)
        assert(db_user.is_staff == True)
        assert(db_user.is_superuser == True)
        assert(db_user.email == "l1234@mail.ru")
        assert(db_user.password == "secure_password")
        assert(db_user.login == "nah")

        CustomUserRepository.update_by_pk(TestCustomUserRepository.client_user, 1, {'email': "testing@mail.ru", 'login' : "testing"})
        db_user = CustomUserRepository.read_by_pk(TestCustomUserRepository.client_user, 1)

        assert(db_user.email == "testing@mail.ru")
        assert(db_user.login == "testing")

        CustomUserRepository.delete_by_pk(TestCustomUserRepository.client_user, 1)
        delete_flag = 0
        try:
            CustomUserRepository.read_by_pk(TestCustomUserRepository.client_user, 1)
        except:
            delete_flag = 1
        assert(delete_flag == 1)

    @staticmethod
    def test_user_CRUD():
        user = CustomUser(
        pk = 1,
        email = "1234@mail.ru",
        password = "secure_password",
        role = 0,
        login = "1234qwerty"
        )

 
        CustomUserRepository.create(TestCustomUserRepository.client_user, user)


        db_user = CustomUserRepository.read_by_pk(TestCustomUserRepository.client_user, 1)

        assert(db_user.id == 1)
        assert(db_user.is_staff == False)
        assert(db_user.is_superuser == False)
        assert(db_user.email == "1234@mail.ru")
        assert(db_user.password == "secure_password")
        assert(db_user.login == "1234qwerty")

        CustomUserRepository.update_by_pk(TestCustomUserRepository.client_user, 1, {'email': "updated@mail.ru", 'login' : "updated"})
        db_user = CustomUserRepository.read_by_pk(TestCustomUserRepository.client_user, 1)

        assert(db_user.email == "updated@mail.ru")
        assert(db_user.login == "updated")

        CustomUserRepository.delete_by_pk(TestCustomUserRepository.client_user, 1)
        delete_flag = 0
        try:
            CustomUserRepository.read_by_pk(TestCustomUserRepository.client_user, 1)
        except:
            delete_flag = 1
        assert(delete_flag == 1)
    
    @staticmethod
    def test_specialist_CRUD():
        user = CustomUser(
        pk = 1,
        email = "test@mail.ru",
        password = "secure_password",
        role = 1,
        login = "testqwerty",
        is_staff = True
        )

 
        CustomUserRepository.create(TestCustomUserRepository.client_user, user)


        db_user = CustomUserRepository.read_by_pk(
        TestCustomUserRepository.client_user, 1)

        assert(db_user.id == 1)
        assert(db_user.is_staff == True)
        assert(db_user.is_superuser == False)
        assert(db_user.email == "test@mail.ru")
        assert(db_user.password == "secure_password")
        assert(db_user.login == "testqwerty")

        CustomUserRepository.update_by_pk(TestCustomUserRepository.client_user, 1, {'email': "changed@mail.ru", 'login' : "changed"})
        db_user = CustomUserRepository.read_by_pk(TestCustomUserRepository.client_user, 1)

        assert(db_user.email == "changed@mail.ru")
        assert(db_user.login == "changed")

        CustomUserRepository.delete_by_pk(TestCustomUserRepository.client_user, 1)
        delete_flag = 0
        try:
            CustomUserRepository.read_by_pk(TestCustomUserRepository.client_user, 1)
        except:
            delete_flag = 1
        assert(delete_flag == 1)


class TestCustomUserService(TestCase):

    @staticmethod
    def test_create_method_service_dependency_with_repository():
        user = AdminUser().user
        mock = MagicMock()
        customUserService = CustomService(mock)
        customUserService.create(user, user)
        mock.create.assert_called_with(user, user)

    @staticmethod
    def test_read_by_pk_method_service_dependency_with_repository():
        user = AdminUser().user
        mock = MagicMock()
        customUserService = CustomService(mock)
        customUserService.read_by_pk(user, 1)
        mock.read_by_pk.assert_called_with(user, 1)