# # Without Redis:
# # import today
# from django_redis import cache
#
# from inteview.models import *
#
# slots = Booking.objects.filter(date=today)  # Hits DB
#
# # With Redis:
# slots = cache.get("today_slots")
# if not slots:
#     slots = Booking.objects.filter(date=today)
#     cache.set("today_slots", slots, timeout=300)
