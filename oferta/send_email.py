from turtle import ht

from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.conf import settings

def send_email(recipient: User, subject, template, context, sender:User = None):
    html_message = render_to_string(template, context)
    if sender is not None and sender.email:
        from_email = sender.email
    else:
        from_email = settings.SYSTEM_EMAIL_ADDRESS

    recipient.email_user(subject, 'email here', from_email, html_message=html_message)


