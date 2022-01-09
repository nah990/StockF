from django.test import TestCase
from .repositories import *
from users.models import CustomUser

class TestRepositoryPattern(TestCase):

    client_user = CustomUser(role=CustomUser.ADMIN)
    @staticmethod
    def test_user_creation_and_updating():
        user = CustomUser(
        email = "1234@mail.ru",
        password = "secure_password",
        role = 0,
        login = "1234qwerty"
        )

 
        CustomUserRepository.create(TestRepositoryPattern.client_user, user)


        db_user = CustomUserRepository.read_by_pk(
        TestRepositoryPattern.client_user, 1)

        assert(db_user.id == 1)
        assert(db_user.is_staff == False)
        assert(db_user.is_superuser== False)
        assert(db_user.email == "1234@mail.ru")
        assert(db_user.password == "secure_password")
        assert(db_user.login == "1234qwerty")

        CustomUserRepository.update_by_pk(TestRepositoryPattern.client_user, 1, {'email': "updated@mail.ru", 'login' : "updated"})
        db_user = CustomUserRepository.read_by_pk(TestRepositoryPattern.client_user, 1)

        assert(db_user.email == "updated@mail.ru")
        assert(db_user.login == "updated")

        CustomUserRepository.delete_by_pk(TestRepositoryPattern.client_user, 1)
        delete_flag = 0
        try:
            CustomUserRepository.read_by_pk(TestRepositoryPattern.client_user, 1)
        except:
            delete_flag = 1
        assert(delete_flag == 1)
