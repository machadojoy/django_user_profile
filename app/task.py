from celery import shared_task
from django.core.mail import EmailMessage

@shared_task
def add(x, y):
    return x + y

@shared_task
def send_new_user_email(to_email):
    email = EmailMessage(
        subject="Your new profile has been created",
        body="Thank you for creating your new profile",
        from_email="test@test.com",
        to=[to_email],
    )
    email.content_subtype = 'html'
    email.send(fail_silently=False)