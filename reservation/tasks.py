from decimal import Decimal
from celery import shared_task
from .models import ReservationTest
from django.utils import timezone


@shared_task
def add_payment():
    reservations = ReservationTest.objects.filter(documentation__status='A')
    sum_pyment = 0
    for reservation in reservations:
        condition2 = (timezone.now() - reservation.created).days

        sum_pyment += reservation.pyment
        # محدودیت پرداخت کمتر
        if sum_pyment < Decimal('3000000.0'):
            # دونگ روزانه
            if (reservation.user.status == 'N' and condition2 > 1) or (
                    reservation.user.status == 'S' and condition2 > 2):
                if len(reservations) == 3:
                    reservation.pyment += Decimal('700.0')
                    reservation.save()
                else:
                    reservation.pyment += Decimal('1000.0')
                    reservation.save()
        # محدودیت زمان
        if (reservation.user.status == 'N' and condition2 > 7) or \
                (reservation.user.status == 'S' and condition2 > 14):
            reservation.documentation.status = 'A'
            reservation.documentation.save()
