import psycopg
from model.account import Account

class AccountsDao:

    def get_all_accounts_by_customer_id(self, customer_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="prj0", user="postgres",
                             password="1234") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts WHERE customer_id = %s", (customer_id,))

                accounts_list = []

                for row in cur:
                    accounts_list.append(Account(row[0], row[1], row[2], row[3]))

                return accounts_list
