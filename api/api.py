import settings
import requests

friends_friends = {}
current_users = {}


def main(user_id=settings.USER_ID, token=settings.ACCESS_TOKEN, count=10):
    friends = (requests.get("https://api.vk.com/method/friends.get", params={
        "user_id": user_id,
        # "fields": "first_name, last_name",
        "access_token": token,
        "v": 5.52
    })).json()["response"]["items"]
    for id in friends:
        friends_friends[id] = requests.get("https://api.vk.com/method/friends.get", params={
            "user_id": id,
            "access_token": token,
            "v": 5.52
        }).json()
        if 'response' in friends_friends[id]:
            friends_friends[id] = friends_friends[id]['response']['items']
            # print(friends_friends[id])
            for user in friends_friends[id]:
                if (user == user_id) or user in friends:
                    continue
                else:
                    if user in current_users:
                        current_users[user] += 1
                    else:
                        current_users[user] = 1
        else:
            friends_friends.pop(id)
    # print(friends)
    better_not_friends = {}
    while current_users:
        k, v = current_users.popitem()
        better_not_friends[v] = k
    sorted(better_not_friends)
    for i in range(count):
        r = requests.get("https://api.vk.com/method/users.get", params={
            "user_ids": better_not_friends.popitem()[1],
            "access_token": token,
            "v": 5.52
        }).json()
        if 'response' in r:
            print(r['response'])
        if not better_not_friends:
            break
