from kavenegar import *


def send_sms(text):
    try:
        api = KavenegarAPI('4D7844566D316D7236473249386D464B7A652F2F6C32394B49316E6D6A7978716C35587A4378456B734D733D')
        params = { 'sender' : '2000660110', 'receptor': '09128236317', 'message' :'.وب سرویس پیام کوتاه کاوه نگار' }
        response = api.sms_send(params)
    except Exception as e:
        print(e)
send_sms("salaam")