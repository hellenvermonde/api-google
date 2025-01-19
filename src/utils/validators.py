''' Utilidade responsável por validar informações recebidas pela API
'''


def validate_email(email):

    """Check if the email address is valid."""
    import re
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(regex, email):
        return True
    return False

def validate_date(date_str):
    """Check if the date string is in the correct format."""
    from datetime import datetime
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False