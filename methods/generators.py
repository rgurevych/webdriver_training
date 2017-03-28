from datetime import *

def generate_email():
    now_str = datetime.isoformat(datetime.today())
    email = now_str[8:10] + now_str[5:7] + '_' + now_str[11:13] + now_str[14:16] + now_str[17:19] + "@mailinator.com"
    print("E-mail for registration: ", email)
    return email

def generate_product_name():
    now_str = datetime.isoformat(datetime.today())
    name = "Butterfly" + now_str[11:13] + now_str[14:16] + now_str[17:19]
    return name

def generate_code():
    now_str = datetime.isoformat(datetime.today())
    code = now_str[8:10] + now_str[5:7] + now_str[11:13] + now_str[14:16] + now_str[17:19]
    return code