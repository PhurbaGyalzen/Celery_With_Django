from time import sleep
from django.conf import settings
from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_feedback_email_task(email_address, message):
    """Sends an email when the feedback form has been submitted."""
    send_mail(
        subject='FeedBack',
        message=f'{message}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email_address,],
        fail_silently=False,
    )

