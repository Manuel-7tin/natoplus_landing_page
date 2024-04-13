import smtplib
import socket
from email.message import EmailMessage
import ssl
from validate_email import validate_email

is_valid = validate_email(
    email_address='ebifredrick07@gmail.com',
    check_format=True,
    check_blacklist=True,
    check_dns=True,
    dns_timeout=10,
    check_smtp=True,
    smtp_timeout=10,
    smtp_helo_host=None,
    smtp_from_address=None,
    smtp_skip_tls=False,
    smtp_tls_context=None,
    smtp_debug=False,)

print(is_valid)

# Get local server hostname


# def verify_email(email):
#     try:
#         try:
#             # Establish a connection to the recipient's SMTP server
#             with smtplib.SMTP() as smtp:
#                 smtp.set_debuglevel(0)  # Optionally set debug level
#                 smtp.connect("smtp.gmail.com", 465)  # Replace with the recipient's SMTP server
#                 # smtp.helo()
#                 smtp.ehlo()
#                 smtp.login("opolopthings@gmail.com", "lozqjciqzvsibxza")  # Replace with your email address
#                 code, message = smtp.rcpt(email)
#                 smtp.quit()
#
#             # If the SMTP server responds with a success code (250), the email exists
#             if code == 250:
#                 print("Email exists")
#                 return True
#             else:
#                 print("Email does not exist")
#                 print(code)
#                 return False
#
#         except smtplib.SMTPException as e:
#             print("Error:", e)
#             return False
#     except socket.gaierror as e:
#         print("The err is:", e)
#
# # Test the function
# email_to_check = "ebifredricks@gmail.com"
# verify_email(email_to_check)
