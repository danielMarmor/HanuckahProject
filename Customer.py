class Customer:
    def __init__(self, id, fname, lname, address, mobile):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.address = address
        self.mobile = mobile

    def __str__(self):
        return f'Customer(Id = {self.id}, First Name = {self.fname}, Last Name = {self.lname}, ' \
               f'Address = {self.address}, Mobile = {self.mobile})'

    def __repr__(self):
        return f'Customer({self.id}, {self.fname}, {self.lname}, {self.address}, {self.mobile})'

    @staticmethod
    def validate_customer_id(cust_id_str: str):
        if cust_id_str == '':
            print('Please Enter Valid Customer Id')
            return False
        if not cust_id_str.isnumeric():
            print('Customer Id Must Be Numeric')
            return False
        cust_id = int(cust_id_str)
        if cust_id < 0:
            print('Customer Id Must Be Positive')
        return True

    @staticmethod
    def validate_fname(fname: str):
        if fname == '':
            print('Please Enter Valid First Name')
            return False
        return True

    @staticmethod
    def validate_lname(fname: str):
        if fname == '':
            print('Please Enter Valid Last Name')
            return False
        return True

    @staticmethod
    def validate_address(address: str):
        if address == '':
            print('Please Enter Valid Adress')
            return False
        return True

    @staticmethod
    def validate_mobile(mobile: str):
        if mobile == '':
            print('Please Enter Valid Mobile')
            return False
        not_numeric_values = [letter for letter in mobile.split() if not letter.isnumeric()]
        if len(not_numeric_values) > 0:
            print('Mobile Must Be All Numeric!')
            return False
        return True

