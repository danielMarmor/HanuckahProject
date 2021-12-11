from Customer import Customer
from CustomerDataAccess import CustomerDataAccess
from enum import Enum


# ENUM SELECTION
class UserSelection(Enum):
    get_all = '1',
    get_cust_by_id = '2',
    insert = '3',
    delete = '4',
    update = '5',
    exit = '6'


# PRINT MENU:
def get_select_menu():
    select_menu = f'Select:\n1. Get all customers\n2. Get customer by id\n3. Insert customer\n' \
                   f'4. Delete customer\n5. Update customer\n6. Exit\n'
    return select_menu


# CONFIRM:
def validate_confirm(is_confirm_str: str):
    if is_confirm_str not in ('0', '1'):
        print('Please Select Validate Confirm!')
        return False
    return True


# MENU OPTIONS :
def menu_cust_by_id(data_access: CustomerDataAccess):
    while True:
        input_cust_id = input('Enter Customer Id: ').strip()
        is_cust_id_valid = Customer.validate_customer_id(input_cust_id)
        if is_cust_id_valid:
            cust_id = int(input_cust_id)
            customer = data_access.get_customers_by_id(cust_id)
            if customer is None:
                print(f'Customer with id: {cust_id} does not exists!')
                break
            print(str(customer))
            break


def menu_input_insert(data_access: CustomerDataAccess):
    cust_id = None
    cust_fname = None
    cust_lname = None
    cust_address = None
    cust_mobile = None
    # ID
    while True:
        input_cust_id = input('Enter Customer Id: ').strip()
        is_cust_id_valid = Customer.validate_customer_id(input_cust_id)
        if is_cust_id_valid:
            cust_id = int(input_cust_id)
            exist_customer_by_id = data_access.get_customers_by_id(cust_id)
            if exist_customer_by_id is not None:
                print(f'Customer With Id {cust_id} allready exists!')
                return
            break
    # FIRST NAME
    while True:
        cust_fname = input('Enter First Name: ').strip()
        is_fname_valid = Customer.validate_fname(cust_fname)
        if is_fname_valid:
            break
    # LAST NAME
    while True:
        cust_lname = input('Enter Last Name: ').strip()
        is_lname_valid = Customer.validate_lname(cust_lname)
        if is_lname_valid:
            break
    # ADDRESS
    while True:
        cust_address = input('Enter Adress: ').strip()
        is_address_valid = Customer.validate_address(cust_address)
        if is_address_valid:
            break
    # MOBILE
    while True:
        cust_mobile = input('Enter Mobile: ').strip()
        is_mobile_valid = Customer.validate_mobile(cust_mobile)
        if is_mobile_valid:
            break
    # CHECK IS EXISTS BY NAME
    exist_customer_by_name = data_access.get_customers_by_name(cust_fname, cust_lname)
    if exist_customer_by_name is not None:
        confirm_insert = None
        while True:
            confirm_insert = input('Customer With exact name allready exists. Are you sure? Yes-1 , No-0: ').strip()
            is_cofirm_validated = validate_confirm(confirm_insert)
            if not is_cofirm_validated:
                continue
            if confirm_insert == '0':
                return
            break
    # *****************
    cust = Customer(cust_id, cust_fname, cust_lname, cust_address, cust_mobile)
    data_access.insert_customer(cust)
    print('Customer Inserted Succesfuly!')
    print(f'Updated List:')
    data_access.print_all_customers()


def menu_input_delete(data_access: CustomerDataAccess):
    input_cust_id = None
    while True:
        input_cust_id = input('Enter Customer Id: ').strip()
        is_cust_id_valid = Customer.validate_customer_id(input_cust_id)
        if is_cust_id_valid:
            cust_id = int(input_cust_id)
            exist_customer = data_access.get_customers_by_id(cust_id)
            if exist_customer is None:
                print(f'Customer With Id {cust_id} not exists!')
                return
            break
    data_access.delete_customer(input_cust_id)
    print('Customer Deleted Succesfuly!')
    print(f'Updated List:')
    data_access.print_all_customers()


def menu_input_update(data_access: CustomerDataAccess):
    cust_id = None
    cust_new_id = None
    cust_fname = None
    cust_lname = None
    cust_address = None
    cust_mobile = None
    # ID
    while True:
        input_cust_id = input('Enter Customer Id: ').strip()
        is_cust_id_valid = Customer.validate_customer_id(input_cust_id)
        if is_cust_id_valid:
            cust_id = int(input_cust_id)
            exist_customer_by_id = data_access.get_customers_by_id(cust_id)
            if exist_customer_by_id is None:
                print(f'Customer With Id {cust_id} not exists!')
                return
            break
    while True:
        input_new_cust_id = input('Enter New Customer Id: ').strip()
        is_new_cust_id_valid = Customer.validate_customer_id(input_new_cust_id)
        if is_new_cust_id_valid:
            cust_new_id = int(input_new_cust_id)
            if cust_new_id != cust_id:
                exist_customer_by_id = data_access.get_customers_by_id(cust_new_id)
                is_cross_customer = exist_customer_by_id is not None
                if is_cross_customer:
                    print(f'Customer With Id {cust_new_id} allready exists!')
                    continue
            break
    # FIRST NAME
    while True:
        cust_fname = input('Enter First Name: ').strip()
        is_fname_valid = Customer.validate_fname(cust_fname)
        if is_fname_valid:
            break
    # LAST NAME
    while True:
        cust_lname = input('Enter Last Name: ').strip()
        is_lname_valid = Customer.validate_lname(cust_lname)
        if is_lname_valid:
            break
    # ADDRESS
    while True:
        cust_address = input('Enter Adress: ').strip()
        is_address_valid = Customer.validate_address(cust_address)
        if is_address_valid:
            break
    # MOBILE
    while True:
        cust_mobile = input('Enter Mobile: ').strip()
        is_mobile_valid = Customer.validate_mobile(cust_mobile)
        if is_mobile_valid:
            break
    cust = Customer(cust_new_id, cust_fname, cust_lname, cust_address, cust_mobile)
    data_access.update_customer(cust_id, cust)
    print('Customer Updated Succesfuly!')
    print(f'Updated List:')
    data_access.print_all_customers()


def manage_customers():
    db_file_path = './Hanuckah.db'
    data_access = CustomerDataAccess(db_file_path)
    while True:
        user_select = input(get_select_menu()).strip()
        if user_select == UserSelection.exit.value[0]:
            break
        if user_select == UserSelection.get_all.value[0]:
            data_access.print_all_customers()
            continue
        if user_select == UserSelection.get_cust_by_id.value[0]:
            menu_cust_by_id(data_access)
            continue
        if user_select == UserSelection.insert.value[0]:
            menu_input_insert(data_access)
            continue
        if user_select == UserSelection.delete.value[0]:
            menu_input_delete(data_access)
            continue
        if user_select == UserSelection.update.value[0]:
            menu_input_update(data_access)
            continue
        print('Please Enter Valid Selection!')
    print('Thank You!')


manage_customers()
