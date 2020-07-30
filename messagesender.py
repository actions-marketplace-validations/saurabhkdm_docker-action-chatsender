from json import dumps
import sys
from httplib2 import Http


def main():
    """Hangouts Chat incoming webhook quickstart."""
    msg = sys.argv[1]
    mod_msg = "Something push against branch"+msg
    url = 'Chat_Channel_web_hook'
    bot_message = {
        'text' : mod_msg}
    

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
