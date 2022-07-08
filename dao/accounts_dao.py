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

    def get_account_by_customer_id_and_account_id(self, customer_id, account_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="prj0", user="postgres",
                             password="1234") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts WHERE customer_id = %s AND id = %s", (customer_id, account_id))

                account_row = cur.fetchone()
                if not account_row:
                    return None

                c_id = account_row[0]
                balance = account_row[1]
                customer_id = account_row[2]
                account_type_id = account_row[3]

                return Account(c_id, balance, customer_id, account_type_id)

    def delete_account_by_customer_id_and_account_id(self, customer_id, account_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="prj0", user="postgres",
                             password="1234") as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM accounts WHERE customer_id = %s and id = %s", (customer_id, account_id))

                rows_deleted = cur.rowcount

                if rows_deleted != 1:
                    return False
                else:
                    conn.commit()
                    return True

    def add_account_for_customer(self, account_object):

        balance_to_add = account_object.balance
        type_to_add = account_object.account_type_id
        customer_id_to_add = account_object.customer_id


        with psycopg.connect(host="127.0.0.1", port="5432", dbname="prj0", user="postgres", password="1234") as conn:

            with conn.cursor() as cur:
                cur.execute("INSERT INTO accounts (balance, customer_id, account_type_id) VALUES (%s, %s, %s) RETURNING *",
                            (balance_to_add, type_to_add, customer_id_to_add))

                account_row = cur.fetchone()

                conn.commit()

                return Account(account_row[0], account_row[1], account_row[2], account_row[3])

    def update_account_for_customer(self, account_object):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="prj0", user="postgres", password="1234") as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE accounts SET account_type_id = %s, balance = %s WHERE id = %s and customer_id = %s RETURNING *",
                            (account_object.account_type_id, account_object.balance, account_object.id, account_object.customer_id))

                conn.commit()

                account_row = cur.fetchone()
                if account_row is None:
                    return None

                return Account(account_row[0], account_row[1], account_row[2], account_row[3])





