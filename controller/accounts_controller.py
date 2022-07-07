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



