import sqlite3
from Customer import Customer


class CustomerDataAccess:
    def __init__(self, path):
        self.cur = sqlite3.connect(path)

    def get_all_customers(self):
        customers = self.cur.execute('Select * from Customer')
        fields = {desc[1][0]: desc[0] for desc in enumerate(customers.description)}
        lst_customers = [Customer(
            int(cust[fields['Id']]),
            str(cust[fields['FirstName']]),
            str(cust[fields['LastName']]),
            str(cust[fields['Address']]),
            str(cust[fields['Mobile']])
        ) for cust in customers]
        return lst_customers

    def print_all_customers(self):
        lst_customers = self.get_all_customers()
        # also posible print(lst_customers)
        print_str = ''
        for cust in lst_customers:
            print_str += f'{str(cust)}\n'
        print(print_str)

    def get_customers_by_id(self, customer_id: int):
        exec_select = f'Select * from Customer where Id={customer_id}'
        exec_cust = self.cur.execute(exec_select)
        columns = {desc[1][0]: desc[0] for desc in enumerate(exec_cust.description)}
        cust = exec_cust.fetchone()
        if cust is None:
            return None
        customer = Customer(int(cust[columns['Id']]), str(cust[columns['FirstName']]), str(cust[columns['LastName']]),
                            str(cust[columns['Address']]), str(cust[columns['Mobile']]))
        return customer

    def get_customers_by_name(self, fname, lname):
        exec_select = f'Select * from Customer where FirstName="{fname}" and LastName ="{lname}"'
        cust = self.cur.execute(exec_select).fetchone()
        return cust

    def insert_customer(self, cust: Customer):
        exist_customer = self.get_customers_by_id(cust.id)
        exec_insert = f'Insert Into Customer Values({cust.id}, "{cust.fname}", "{cust.lname}",' \
                      f'"{cust.address}", "{cust.mobile}")'
        self.cur.execute(exec_insert)
        self.cur.commit()

    def update_customer(self, cust_id, cust: Customer):
        exist_customer = self.get_customers_by_id(cust.id)
        exec_update = f'Update Customer Set Id={cust.id}, FirstName="{cust.fname}", LastName="{cust.lname}",' \
                      f'Address="{cust.address}", Mobile="{cust.mobile}" where Id={cust_id}'
        self.cur.execute(exec_update)
        self.cur.commit()

    def delete_customer(self, customer_id):
        exist_customer = self.get_customers_by_id(customer_id)
        if exist_customer is None:
            print(f'Customer Not Exists With Id ={customer_id}')
            return
        exec_delete = f'Delete From Customer where Id={customer_id}'
        self.cur.execute(exec_delete)
        self.cur.commit()
