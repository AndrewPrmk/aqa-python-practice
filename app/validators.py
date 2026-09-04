def validate_registration(email, username, password, confirm_password, accept_terms):
    errors = {}

    if not email or "@" not in email:
        errors["email"] = "Email is invalid"

    elif not username or len(username) < 3 or len(username) > 20:
        errors["username"] = "Username is invalid"

    elif not password or len(password) < 8:
        errors["password"] = "Password is invalid"

    elif not confirm_password or confirm_password != password:
        errors["email"] = "Confirm_password is invalid"

    elif accept_terms != True:
        errors["email"] = "Accept_terms is invalid"

    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }

def validate_login(email, password, remember_me):
    errors = {}

    if not email:
        errors["email"] = "Email is required"
    elif "@" not in email:
        errors["email"] = "Email is invalid"

    if not password:
        errors["password"] = "Password is required"
    elif len(password) < 8:
        errors["password"] = "Password is invalid"

    if type(remember_me) is not bool:
        errors["remember_me"] = "Remember me must be boolean"

    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }

def validate_registration(email, username, password, confirm_password, accept_terms):
    errors = {}

    if not email:
        errors["email"] = "Email is required"
    elif "@" not in email:
        errors["email"] = "Email is invalid"

    if not username:
        errors["username"] = "Username is required"
    elif len(username) < 3 or len(username) > 20:
        errors["usernae"] = "Username is invalid"

    if not password:
        errors["password"] = "Password is required"
    elif len(password) < 8:
        errors["password"] = "Password is invalid"

    if not confirm_password:
        errors["confirm_password"] = "Confirm password is required"
    elif password != confirm_password:
        errors["confirm_password"] = "Confirm password is invalid"

    if accept_terms is not True:
        errors["accept_terms"] = "Accept terms is invalid"

    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }