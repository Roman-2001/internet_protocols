import api
import argparse

if __name__ == '__main__':
    print('Программа выводит количество недрузей, упорядоченных по убыванию числа общих друзей')
    print("Input your access token")
    access_token = str(input())
    print("Input your user_id")
    user_id = str(input())
    print("Input count of not friends or press enter (default=10)")
    try:
        count = int(input())
    except Exception:
        count = 10
    api.main(user_id, access_token, count)
