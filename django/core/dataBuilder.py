from users.models import CustomUser
from stock.services import CustomUserService
from stock.models import SourceInfo, StockInfo, StockByDate

class UserBuilder:
    def __init__(self):
        self.user = None
        self.get_user()

    def get_user(self):
        raise NotImplementedError

class SuperUser(UserBuilder):
    def get_user(self):
        self.user = CustomUser(
            pk=1,
            email="l1234@mail.ru",
            password="secure_password",
            role=2,
            username="nah",
            is_staff=True,
            is_superuser=True
        )

class User(UserBuilder):
    def get_user(self):
        self.user = CustomUser(
            pk=1,
            email="l1234@mail.ru",
            password="secure_password",
            role=0,
            username="nah"
        )

class AdminUser(UserBuilder):
    def get_user(self):
        self.user = CustomUser(
            pk=1,
            email="l1234@mail.ru",
            password="secure_password",
            role=2,
            username="nah",
            is_staff=True,
            is_superuser=True
        )
        
class SpecialistUser(UserBuilder):
    def get_user(self):
        self.user = CustomUser(
            pk=1,
            email="l1234@mail.ru",
            password="secure_password",
            role=1,
            username="nah",
            is_staff=True
        )

class DefaultUser(UserBuilder):
    def get_user(self):
        self.user = CustomUser(
            pk=1,
            email="l1234@mail.ru",
            password="secure_password",
            role=4,
            username="nah",
            is_staff=True,
            is_superuser=True
        )

class UserBuilderByPk:
    def __init__(self, pk):
        self.customuser = CustomUser(
            pk=1,
            email="l1234@mail.ru",
            password="secure_password",
            role=0,
            username="nah"
        )
        self.user = None
        self.pk = pk
        self.get_user()

    def get_user(self):
        raise NotImplementedError

class UserByPk(UserBuilderByPk):

    def get_user(self):
        self.user = CustomUserService.read_by_pk(self.customuser, self.pk)

class SourceInfoBuilder:
    def build(self):
        sourceInfo = SourceInfo(
        name = "Test",
        rating = 1,
        )
        return sourceInfo

class StockInfoBuilder:
    def build(self):
        stockInfo = StockInfo(
        name = "TestName",
        ticket = "TestTicket",
        source_id = SourceInfoBuilder.build.id,
        )
        return stockInfo

class StockByDateBuilder:
    def build(self):
        stockByDate = StockByDate(
        ticket_id = StockInfoBuilder.build.id,
        min_price = 1,
        avg_price = 2,
        max_price = 3,
        forecast_date = '2022-01-09',
        outdated_status = False,
        final_accuracy = 1,
        )
        return stockByDate
