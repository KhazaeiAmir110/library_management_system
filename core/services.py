import os
import sys
from core import redis_services


def create_otp(key, header=None, length=5, **options):
    otp = str(int.from_bytes(os.urandom(int(length / 2)), sys.byteorder))
    otp = otp[:length]
    if len(otp) < length:
        otp = otp.zfill(length)

    redis_services.set(redis_services.make_key(key, header), otp, **options)
    return otp


def is_otp_match(otp, key, header=None, **options):
    result_otp = redis_services.get(redis_services.make_key(key, header))
    if result_otp is None or result_otp.decode('utf-8') != otp:
        return False

    return True
