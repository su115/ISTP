import requests
import json
import logging

import time

logging.basicConfig(
    filename="/mylog/server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)


def main(url):
    while True:
        try: 
            r = requests.get(url)
            data = json.loads(r.content)
            logging.info("Сервер доступний. Час на сервері: %s", data['date'])
            logging.info("Запитувана сторінка: : %s", data['server_url'])
            logging.info("Відповідь сервера місти наступні поля:")
            for key in data.keys():
                logging.info("Ключ: %s, Значення: %s", key, data[key])
        except requests.exceptions.ConnectionError as e:
            logging.error("Unable to conect to the server: " + str(e))

        time.sleep(60)

if __name__ == '__main__':
    main("http://mysite:8000/json")
