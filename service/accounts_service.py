from dao.accounts_dao import AccountsDao
from dao.customer_dao import CustomerDao
from exception.customer_not_found import CustomerNotFoundError


class AccountsService:

    def __init__(self):
        self.accounts_dao = AccountsDao()
        self.customer_dao = CustomerDao()

    def get_all_accounts_by_customer_id(self, customer_id):
        if self.customer_dao.get_customer_by_id(customer_id) is None:
            raise CustomerNotFoundError(f"Customer with id {customer_id} was not found")

        return list(map(lambda a: a.to_dict(), self.accounts_dao.get_all_accounts_by_customer_id(customer_id)))


    def get_account_by_customer_id_and_account_id(self, customer_id, account_id):
        account_obj = self.accounts_dao.get_account_by_customer_id_and_account_id(customer_id, account_id)

        if not account_obj:
            raise CustomerNotFoundError(f"Customer with id {customer_id} was not found")

        return account_obj.to_dict()

    def delete_account_by_customer_id_and_account_id(self, customer_id, account_id):
        if not self.accounts_dao.delete_account_by_customer_id_and_account_id(customer_id, account_id):
            raise CustomerNotFoundError(f"Customer with id {account_id} was not found")

