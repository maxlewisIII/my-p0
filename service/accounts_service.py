from dao.accounts_dao import AccountsDao
from dao.customer_dao import CustomerDao
from exception.customer_not_found import CustomerNotFoundError


class AccountsService:

    def __init__(self):
        self.accounts_dao = AccountsDao()
        self.customer_dao = CustomerDao()

    def get_all_accounts_by_customer_id(self, customer_id):
        if self.customer_dao.get_customer_by_id(customer_id) is None:
            raise CustomerNotFoundError(f"User with id {customer_id} was not found")

        return list(map(lambda a: a.to_dict(), self.accounts_dao.get_all_accounts_by_customer_id(customer_id)))