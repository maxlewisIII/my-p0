import dao.customer_dao
from exception.invalid_parameter import InvalidParameterError
from exception.customer_not_found import CustomerNotFoundError
from model.customer import Customer
from service.customer_service import CustomerService
import pytest


def test_get_all_customers(mocker):
    def mock_get_all_customers(self):
        return [Customer(1, 'name'), Customer(2, 'name2')]

    mocker.patch('dao.customer_dao.CustomerDao.get_all_customers', mock_get_all_customers)

    customer_service = CustomerService()

    actual = customer_service.get_all_customers()

    assert actual == [
        {
            "id": 1,
            "first name": "name"
        },
        {
            "id": 2,
            "first name": "name2"
        },
    ]