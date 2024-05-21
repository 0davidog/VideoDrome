from django.conf import settings
from django.template.loader import render_to_string

def send_customer_message(message):

    """
    Function to send the customer an order confirmation email.
    Called from webhook_handler.py when payment_intent.succeeded.
    related to CustomerOrder model as argument 
    Uses email account referenced in env vars.
    """

    # retrieve customer email from order object passed to function.
    customer_email = message.user_email

    # import EmailMessage module within function to avoid circular import errors
    from django.core.mail import EmailMessage
    
    # retrieve email address from env vars.
    sender_email = settings.EMAIL_HOST_USER

    # Email address to send to
    recipient_list = [customer_email]

    # Email Subject
    email_subject = message.subject

    # Email body imported from seperate body_order_confirmation.html file.
    # order and sender email provided as context
    email_body = message.body
    
    # Complie all the information into an email.
    email = EmailMessage(email_subject, email_body, sender_email, recipient_list)
    email.content_subtype = "html"  # Set the content type to HTML
    email.send() # Email sent.