import re

def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

# Test the extract_emails function
text = "Please contact support@example.com for assistance or sales@example.com for inquiries."
result = extract_emails(text)
print(result)  # Output: ['support@example.com', 'sales@example.com']
