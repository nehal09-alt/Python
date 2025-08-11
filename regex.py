import re

# Email validate karna
text = "Mera email hai grok@xai.com aur dusra hai test@123.com"
pattern = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
emails = re.findall(pattern, text)
print(emails)  # Output: ['grok@xai.com', 'test@123.com']

# Phone number dhundna
text = "Mera number hai 123-456-7890 aur 9876543210"
pattern = r'\d{3}-\d{3}-\d{4}'
phone = re.search(pattern, text)
print(phone.group())  # Output: 123-456-7890

# Text replace karna
text = "Hello 123, Hello 456"
new_text = re.sub(r'\d+', 'XXX', text)
print(new_text)  # Output: Hello XXX, Hello XXX