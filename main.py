import argparse
import requests
import telegram
from environs import Env
from time import sleep


def main():
    env = Env()
    env.read_env()
    tg_bot_token = env.str('TG_BOT_TOKEN')
    dvmn_token = env.str('DVMN_TOKEN')
    tg_chat_id = env.str('TG_CHAT_ID')

    bot = telegram.Bot(token=tg_bot_token)

    url = 'https://dvmn.org/api/long_polling/'
    headers = {'Authorization': dvmn_token}
    params = None

    while True:
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            attempt = response.json()
        except requests.exceptions.Timeout:
            print('timeout')
            continue
        except requests.ConnectionError:
            print('ConnectionError')
            sleep(5)
            continue
        if attempt['status'] == 'timeout':
            timestamp = attempt['timestamp_to_request']
            params = {'timestamp': timestamp}
            continue

        timestamp = attempt['last_attempt_timestamp']
        params = {'timestamp': timestamp}

        lesson_title = attempt['new_attempts'][0]['lesson_title']
        is_negative = attempt['new_attempts'][0]['is_negative']
        lesson_url = attempt['new_attempts'][0]['lesson_url']

        if is_negative:
            bot.send_message(text=f"У Вас проверили работу \"{lesson_title}\".\n"
                                  f"К сожалению, в работе нашлись ошибки.\n{lesson_url}",
                             chat_id=tg_chat_id)
            continue

        bot.send_message(text=f"У Вас проверили работу \"{lesson_title}\".\n"
                              f"Преподавателю все понравилось. Можно приступать к следующему уроку!",
                         chat_id=tg_chat_id)


if __name__ == "__main__":
    main()
