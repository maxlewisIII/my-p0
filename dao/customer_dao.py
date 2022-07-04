from model.customer import Customer
import psycopg
import copy


class CustomerDao:
    def get_all_customers(self):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="prj0", user="postgres", password="1234") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers")

                my_list_of_customer_objs = []

                for customer in cur:
                    c_id = customer[0]
                    first_name = customer[1]



                    my_customer_obj = Customer(c_id, first_name)
                    my_list_of_customer_objs.append(my_customer_obj)

                return my_list_of_customer_objs

    def get_customer_by_id(self, customer_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="prj0", user="postgres", password="1234") as conn:
            with conn.cursor() as cur:

                cur.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))

                customer_row = cur.fetchone()
                if not customer_row:
                    return None

                c_id = customer_row[0]
                first_name = customer_row[1]

                return Customer(c_id, first_name)


