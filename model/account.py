class Account:
    def __init__(self, a_id, balance, customer_id, account_type_id):
        self.id = a_id
        self.balance = balance
        self.customer_id = customer_id
        self.account_type_id = account_type_id

    def to_dict(self):
        return {
            "ID": self.id,
            "Balance": self.balance,
            "Customer ID": self.customer_id,
            "Account Type ID": self.account_type_id
        }


