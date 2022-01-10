from django.test import TestCase
from .repositories import *
from .models import *
from users.models import CustomUser

class TestSourceInfoRepository(TestCase):

    client_user = CustomUser(role=CustomUser.DEFAULT)
    @staticmethod
    def test_crud():
        sourceInfo = SourceInfo(
        name = "Test",
        rating = 1,
        )
 
        SourceInfoRepository.create(TestSourceInfoRepository.client_user, sourceInfo)


        db_sourceInfo = SourceInfoRepository.read_by_pk(
        TestSourceInfoRepository.client_user, 1)

        assert(db_sourceInfo.id == 1)
        assert(db_sourceInfo.name == "Test")
        assert(db_sourceInfo.rating== 1)

        SourceInfoRepository.update_by_pk(TestSourceInfoRepository.client_user, 1, {'name': "ABC", 'rating' : 2})
        db_sourceInfo = SourceInfoRepository.read_by_pk(TestSourceInfoRepository.client_user, 1)

        assert(db_sourceInfo.name == "ABC")
        assert(db_sourceInfo.rating == 2)

        SourceInfoRepository.delete_by_pk(TestSourceInfoRepository.client_user, 1)
        delete_flag = 0
        try:
            SourceInfoRepository.read_by_pk(TestSourceInfoRepository.client_user, 1)
        except:
            delete_flag = 1
        assert(delete_flag == 1)


class TestStockInfoRepository(TestCase):

    client_user = CustomUser(role=CustomUser.DEFAULT)
    @staticmethod
    def test_crud():
        sourceInfo = SourceInfo(
        name = "Test",
        rating = 1,
        )

        stockInfo = StockInfo(
        name = "TestName",
        ticket = "TestTicket",
        source_id = sourceInfo.id,
        )
 
        StockInfoRepository.create(TestStockInfoRepository.client_user, stockInfo)


        db_stockInfo = StockInfoRepository.read_by_pk(
        TestStockInfoRepository.client_user, 1)

        assert(db_stockInfo.id == 1)
        assert(db_stockInfo.name == "TestName")
        assert(db_stockInfo.ticket == "TestTicket")

        StockInfoRepository.update_by_pk(TestStockInfoRepository.client_user, 1, {'name': "ABC", 'ticket' : "TICKET"})
        db_stockInfo = StockInfoRepository.read_by_pk(TestStockInfoRepository.client_user, 1)

        assert(db_stockInfo.name == "ABC")
        assert(db_stockInfo.ticket == "TICKET")

        StockInfoRepository.delete_by_pk(TestStockInfoRepository.client_user, 1)
        delete_flag = 0
        try:
            StockInfoRepository.read_by_pk(TestStockInfoRepository.client_user, 1)
        except:
            delete_flag = 1
        assert(delete_flag == 1)

class TestStockByDateRepository(TestCase):

    client_user = CustomUser(role=CustomUser.DEFAULT)
    @staticmethod
    def test_crud():
        sourceInfo = SourceInfo(
        name = "Test",
        rating = 1,
        )

        stockInfo = StockInfo(
        name = "TestName",
        ticket = "TestTicket",
        source_id = sourceInfo.id,
        )

        stockByDate = StockByDate(
        ticket_id = stockInfo.id,
        min_price = 1,
        avg_price = 2,
        max_price = 3,
        forecast_date = '2022-01-09',
        outdated_status = False,
        final_accuracy = 1,
        )
 
        StockByDateRepository.create(TestStockByDateRepository.client_user, stockByDate)


        db_stockByDate = StockByDateRepository.read_by_pk(
        TestStockByDateRepository.client_user, 1)

        assert(db_stockByDate.id == 1)
        assert(db_stockByDate.min_price == 1)
        assert(db_stockByDate.avg_price == 2)
        assert(db_stockByDate.max_price == 3)
        assert(str(db_stockByDate.forecast_date) == '2022-01-09')
        assert(db_stockByDate.outdated_status == False)
        assert(db_stockByDate.final_accuracy == 1)

        StockByDateRepository.update_by_pk(TestStockByDateRepository.client_user, 1, {'min_price': 5, 
                                                                                      'avg_price' : 6,
                                                                                      'max_price' : 7,
                                                                                      'forecast_date' : '2022-01-06',
                                                                                      'outdated_status' : True,
                                                                                      'final_accuracy' : 2})
        db_stockByDate = StockByDateRepository.read_by_pk(TestStockByDateRepository.client_user, 1)

        assert(db_stockByDate.min_price == 5)
        assert(db_stockByDate.avg_price == 6)
        assert(db_stockByDate.max_price == 7)
        assert(str(db_stockByDate.forecast_date) == '2022-01-06')
        assert(db_stockByDate.outdated_status == True)
        assert(db_stockByDate.final_accuracy == 2)

        StockByDateRepository.delete_by_pk(TestStockByDateRepository.client_user, 1)
        delete_flag = 0
        try:
            StockByDateRepository.read_by_pk(TestStockByDateRepository.client_user, 1)
        except:
            delete_flag = 1
        assert(delete_flag == 1)