from json import dumps
import sys
from httplib2 import Http


def main():
    """Hangouts Chat incoming webhook quickstart."""
    msg = sys.argv[1]
    mod_msg = "Something push against branch"+msg
    url = 'https://chat.googleapis.com/v1/spaces/AAAAW92x_Vw/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=YhnS-MnqheNDK2l4rdddHVN2SZNN_0UbhkLQCZIQ2bM%3D'
    bot_message = {
        'text' : msg}
    

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)

if __name__ == '__main__':
    main()
