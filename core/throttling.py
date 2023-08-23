from django.contrib.auth import get_user_model
from rest_framework.throttling import ScopedRateThrottle


class UserPhoneAuthenticator:
    def authenticate(self, request):
        phone_number = request.data.get('phone_number')
        User = get_user_model()
        try:
            user = User.objects.get(phone_number=phone_number)
            return user, None
        except User.DoesNotExist:
            return None


class UserPhoneRateThrottle(ScopedRateThrottle):
    scope = 'user-otp'
    rate = '10/h'

    def parse_rate(self, rate):
        if rate is None:
            return None, None
        num, period = rate.split('/')
        num_requests = int(num)
        duration = {'s': 1, 'm': 120, 'h': 7200, 'd': 86400}[period[0]]
        return num_requests, duration
