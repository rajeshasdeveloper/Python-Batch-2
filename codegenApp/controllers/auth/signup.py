from utilities.db_utility import db_util

def register(body_data: dict) -> bool:
    try:
        mandatory_list = [
            "email",
            "username",
            "password",
            "confirm_password"
        ]

        for field in mandatory_list:
            if field not in body_data:
                return {
                    "error": "Please fill all the mandatory fields"
                }
        email_validation_result = email_validation(body_data["email"])
        if email_validation_result != True:
            return email_validation_result
        if len(body_data["username"]) <= 1:
            return {
                "error": "invalid username"
            }
        password_validation_result =  password_validation(body_data["password"], body_data["confirm_password"])
        print(password_validation_result)
        if password_validation_result != True:
            return password_validation_result
        
        insert_users(body_data)
    except Exception as err:
        print(err)
        error = {
            "error": "Unknown error"
        }
        if "UNIQUE constraint failed" in str(err):
            error["error"] = "User already exists with the given email"
        return error
    return True


def email_validation(email):
    if "@" not in email:
        return {
            "error": "Invalid email"
        }
    email_domain = email.split('.')[-1]
    if email_domain not in ['org', 'in', 'edu', 'com', 'net', 'web', 'io']:
         return {
            "error": "Invalid email"
        }
    return True

def password_validation(password, confirm_password):
    if password != confirm_password:
         return {
            "error": "password and confirm_password mismatch"
        }
    if len(password) < 6:
         return {
            "error": "minimum length of password is six characters"
        }
    return True


def insert_users(user_data):
    user_insert_query = "INSERT INTO USERS(EMAIL, USERNAME, PASSWORD) VALUES (?,?,?)"
    user_insert_param = [user_data["email"], user_data["username"], user_data["mobile"]]
    db_util(user_insert_query, user_insert_param)

