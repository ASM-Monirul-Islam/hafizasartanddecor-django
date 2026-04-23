from django.conf import settings
from django.core.mail import send_mail
 

def send_confirmation_mail(order_id,  email, name, status):
    subject = f"Your order is {status}"
    email_from = settings.EMAIL_HOST_USER
    message=(f"""
Hello {name},

Your order status for Order {order_id} has been updated to: {status}

Thank you,
Hafiza's Art & Decor
""")
    send_mail(subject, message, email_from, [email])

def send_user_order_mail(order_id, name, phone, email, shipping_method, total_price, address):
    subject=f"Hafiza's Art & Decor"
    email_from = settings.EMAIL_HOST_USER
    email_to = email
    message=(f"""
Hello Dear Customer,

You have placed an order at Hafiza's Art & Decor.

Details:

Order ID: {order_id}
Name: {name}
Email: {email}
Phone: {phone}
Shipping Method: {shipping_method}
Address: {address}
Total Price: {total_price}
             
""")
    send_mail(subject, message, email_from, [email_to])
    
def send_new_order_mail(order_id, name, user_email, phone, shipping_method, address, total_price):
    subject=f"You have got a New Order"
    email_from = settings.EMAIL_HOST_USER
    email_to = settings.EMAIL_HOST_USER
    message=(f"""
Hello Hafiza's Art & Decor,

You have got a new Order

Details:

Order ID: {order_id}
Name: {name}
Email: {user_email}
Phone: {phone}
Shipping Method: {shipping_method}
Address: {address}
Total Price: {total_price}
             
""")
    send_mail(subject, message, email_from, [email_to])
    
    
def send_contact_mail(name, email, message):
    subject=f"Message from Hafiza's Art & Decor"
    email_from = settings.EMAIL_HOST_USER
    email_to = settings.EMAIL_HOST_USER
    main_message=(f"""
Hello Hafiza's Art & Decor,

You have got a message from Hafiza's Art and Decor

Name: {name}
Email: {email}
Message:

{message}
             
""")
    send_mail(subject, main_message, email_from, [email_to])