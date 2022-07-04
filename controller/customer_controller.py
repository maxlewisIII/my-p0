from flask import Blueprint, request
from model.customer import Customer
from service.customer_service import CustomerService
from exception.customer_not_found import CustomerNotFoundError

cc = Blueprint('customer_controller', __name__)

customer_service = CustomerService()

@cc.route('/test')
def test():
    return "test"

@cc.route('/customers')
def get_all_customers():
    return{
        "customers": customer_service.get_all_customers()
    }

@cc.route('/customers/<customer_id>')
def get_customer_by_id(customer_id):
    try:
        return customer_service.get_customer_by_id(customer_id)
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 404


