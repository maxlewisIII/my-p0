from flask import Blueprint

from exception.customer_not_found import CustomerNotFoundError
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












