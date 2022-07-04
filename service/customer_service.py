from dao.customer_dao import CustomerDao

class CustomerService:

    def __init__(self):
        self.customer_dao = CustomerDao()

    def get_all_customers(self):
        list_of_customer_objects = self.customer_dao.get_all_customers()

        list_of_customer_dictionaries = []
        for customer_obj in list_of_customer_objects:
            list_of_customer_dictionaries.append(customer_obj.to_dict())

        return list_of_customer_dictionaries

    def get_customer_by_id(self, customer_id):
        customer_obj = self.customer_dao.get_customer_by_id(customer_id)

        if not customer_obj:
            raise CustomerNotFoundError(f"Customer with id {customer_id} was not found")

        return customer_obj.to_dict()