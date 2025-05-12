import re as regex


email_log = """
User login: john.doe@example.com  
User login: jane.smith@example.com  
User login: john.doe@example.com  
User login: emily.brown@example.com  
User login: mark.jones@example.com  
User login: jane.smith@example.com  
User login: lucas.wilson@example.com  
User login: emily.brown@example.com  
User login: natalie.king@example.com  
User login: john.doe@example.com
"""
# Filtering all the emails based on a REGEX.
print(regex.findall("\w+@\w+\.\w+", email_log))