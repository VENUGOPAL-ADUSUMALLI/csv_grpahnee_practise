# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Booking


@receiver(post_save, sender=Booking)
def booking_created(sender, instance, created, **kwargs):
    if created:
        print(f"Cabin booked by {instance.user.username} from {instance.start_time} to {instance.end_time}")
