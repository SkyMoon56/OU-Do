def is_valid_ou_email(email):
    """
    Checks if a user-provided email is a valid University of Oklahoma address.
    """
    email = email.lower().strip()
    
    # Check if the email ends with the correct domain
    if email.endswith("@ou.edu"):
        return True
    else:
        print(f"Access Denied: {email} is not a valid OU address.")
        return False

# Quick test
user_input = "boomer.sooner@ou.edu"
if is_valid_ou_email(user_input):
    print("Welcome to OU-Do!")
