import re

def is_valid_email(email):
    if not email or not isinstance(email, str):
        return False
        
    # Basic email regex pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def count_valid_emails(emails):
    if not isinstance(emails, list):
        return 0
        
    return sum(1 for email in emails if is_valid_email(email))
