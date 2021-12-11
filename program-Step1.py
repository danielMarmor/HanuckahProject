from Customer import Customer


def get_all_customers(cur):
    customers = cur.execute('Select * from Customer')
    fields = {desc[1][0]: desc[0] for desc in enumerate(customers.description)}
    lst_customers = [Customer(
        int(cust[fields['Id']]),
        str(cust[fields['FirstName']]),
        str(cust[fields['LastName']]),
        str(cust[fields['Address']]),
        str(cust[fields['Mobile']])
    ) for cust in customers]
    return lst_customers


def print_all_customers():
    lst_customers = get_all_customers()
    # also posible print(lst_customers)
    print_str = ''
    for cust in lst_customers:
        print_str += f'{str(cust)}\n'
    print(print_str)


def get_customers_by_id(cur, customer_id: int):
    exec_select = f'Select * from Customer where Id={customer_id}'
    exec_cust = cur.execute(exec_select)
    columns = {desc[1][0]: desc[0] for desc in enumerate(exec_cust.description)}
    cust = exec_cust.fetchone()
    if cust is None:
        return None
    customer = Customer(int(cust[columns['Id']]), str(cust[columns['FirstName']]), str(cust[columns['LastName']]),
                        str(cust[columns['Address']]), str(cust[columns['Mobile']]))
    return customer


def get_customers_by_name(cur, fname, lname):
    exec_select = f'Select * from Customer where FirstName="{fname}" and LastName ="{lname}"'
    cust = cur.execute(exec_select).fetchone()
    return cust


def insert_customer(cur, cust: Customer):
    exist_customer = get_customers_by_id(cust.id)
    exec_insert = f'Insert Into Customer Values({cust.id}, "{cust.fname}", "{cust.lname}",' \
                  f'"{cust.address}", "{cust.mobile}")'
    cur.execute(exec_insert)
    cur.commit()


def update_customer(cur, cust_id, cust: Customer):
    exist_customer = get_customers_by_id(cust.id)
    exec_update = f'Update Customer Set Id={cust.id}, FirstName="{cust.fname}", LastName="{cust.lname}",' \
                  f'Address="{cust.address}", Mobile="{cust.mobile}" where Id={cust_id}'
    cur.execute(exec_update)
    cur.commit()


def delete_customer(cur, customer_id):
    exist_customer = get_customers_by_id(customer_id)
    if exist_customer is None:
        print(f'Customer Not Exists With Id ={customer_id}')
        return
    exec_delete = f'Delete From Customer where Id={customer_id}'
    cur.execute(exec_delete)
    cur.commit()