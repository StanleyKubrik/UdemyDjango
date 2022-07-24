import requests
from .models import TeleSettings


def sendTelegram(tg_id, tg_name, tg_phone):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat_id)
        text = str(settings.tg_message)
        text = text.replace('id', str(tg_id)).replace('name', tg_name).replace('phone', tg_phone)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text
            })
        except:
            pass
        finally:
            if req.status_code != 200:
                print('Ошибка отправки!')
            elif req.status_code == 500:
                print('Ошибка сервера!')
            else:
                print('Сообщение отправлено!')

