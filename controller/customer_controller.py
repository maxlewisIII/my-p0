from flask import Blueprint, request
from model.customer import Customer
from service.customer_service import CustomerService
from exception.customer_not_found import CustomerNotFoundError
from exception.invalid_parameter import InvalidParameterError

cc = Blueprint('customer_controller', __name__)

customer_service = CustomerService()

@cc.route('/test')
def test():
    return "test"


@cc.route('/customers')
def get_all_customers():
    return {
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


@cc.route('/customers/<customer_id>', methods=['DELETE'])
def delete_customer_by_id(customer_id):
    try:
        customer_service.delete_customer_by_id(customer_id)

        return {
            "message": f"Customer with id{customer_id} deleted successfully"
        }
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 404

@cc.route('/customers', methods=['POST'])
def add_customer():
    customer_json_dictionary = request.get_json()
    customer_object = Customer(None, customer_json_dictionary['first_name'])
    try:
        return customer_service.add_customer(customer_object), 201
    except InvalidParameterError as e:
        return {
            "message": str(e)
        }, 400

@cc.route('/customers/<customer_id>', methods=['PUT'])
def update_customer_by_id(customer_id):
    try:
        json_dictionary = request.get_json()
        return customer_service.update_customer_by_id(Customer(customer_id, json_dictionary['first_name']))

    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 404





