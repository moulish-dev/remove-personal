import re

def removeEmailsText(data):
    # Removes emails from data
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' 
    e = re.sub(email_pattern,'',data) # Regular expression used to match email addresses
    
    return e
