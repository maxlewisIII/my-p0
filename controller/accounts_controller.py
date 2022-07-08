from flask import Blueprint, request
from model.account import Account

from exception.customer_not_found import CustomerNotFoundError
from exception.account_not_found import AccountNotFoundError
from exception.invalid_parameter import InvalidParameterError
from service.accounts_service import AccountsService


ac = Blueprint('accounts_controller', __name__)

accounts_service = AccountsService()

@ac.route('/customers/<customer_id>/accounts')
def get_all_accounts_by_customer_id(customer_id):
    try:
        return {
            "accounts": accounts_service.get_all_accounts_by_customer_id(customer_id)
        }
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 404

@ac.route('/customers/<customer_id>/accounts/<account_id>')
def get_account_by_customer_id_and_account_id(customer_id, account_id):
    try:
        return accounts_service.get_account_by_customer_id_and_account_id(customer_id, account_id), 201
    # ADD EXCEPTION AccountNotFoundError
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 404

@ac.route('/customers/<customer_id>/accounts/<account_id>', methods=['DELETE'])
def delete_account_by_customer_id_and_account_id(customer_id, account_id):
    try:
        accounts_service.delete_account_by_customer_id_and_account_id(customer_id, account_id)

        return {
            "message": f"Account with ID {account_id} deleted successfully"
        }
    # ADD EXCEPTION AccountNotFoundError
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 404

@ac.route('/customers/<customer_id>/accounts', methods=['POST'])
def add_account_for_customer(customer_id):
    account_json_dictionary = request.get_json()
    account_object = Account(None, account_json_dictionary['balance'], account_json_dictionary['account_type_id'], customer_id)

    try:
        return accounts_service.add_account_for_customer(account_object), 201
    except InvalidParameterError as e:
        return {
            "message": str(e)
        }, 400

@ac.route('/customers/<customer_id>/accounts/<account_id>', methods=['PUT'])
def update_account_for_customer(customer_id, account_id):
    try:
        account_json_dictionary = request.get_json()
        return accounts_service.update_account_for_customer(Account(account_id, account_json_dictionary['balance'],
                                                                    account_json_dictionary['account_type_id'], customer_id))

    except AccountNotFoundError as e:
        return {
            "message": str(e)
        }, 404











