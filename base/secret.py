import random

# setting
DATABASE_PATH = 'base/database.db'
CSRF_SESSION_KEY = 'CSRF_SESSION_KEY'
SECRET_KEY = 'SECRET_KEY'

ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = ''
SCOPES = ['https://www.googleapis.com/auth']

# random code
code = random.randint(10000, 99999)

# sms
API_KEY = 'hkuxOCaUNfG1sUos7yJ5tNMpvo9yL81z1diapm2jstE='
sender = '3000505'
summary = 'mediana.ir'

# zarinpal
ZP_API_STARTPAY = "https://sandbox.zarinpal.com/pg/StartPay/"
ZARINPAL_WEBSERVICE = "https://sandbox.zarinpal.com/pg/services/WebGate/wsdl"
MERCHANT = '6a525ac8-a09c-4e00-b73c-2c964dc90ab5'

description = 'شما در حال رزرو از سایت براتو هستید.'
email = 'khazaei.amir110@gmail.com'
phone = '09941216569'
