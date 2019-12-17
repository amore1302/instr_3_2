﻿from instabot import Bot
from dotenv import load_dotenv
from pprint import pprint
import argparse
import re
import os



def is_user_exist(current_user):
    return bot.get_user_id_from_username(current_user) is not None 


def get_all_users_from_one_comment(current_comment):
	# как искать регулярное выражение для инстаграмм описано в ссылке
	#     https://blog.jstassen.com/2016/03/code-regex-for-instagram-username-and-hashtags/
    reg_expr_for_user_instagram = "(?:@)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)"
    all_users_from_one_comment = set()
    current_comment_users = re.findall(reg_expr_for_user_instagram, current_comment)
    for current_user in current_comment_users:
        if is_user_exist(current_user):
            all_users_from_one_comment.add(current_user)
    return all_users_from_one_comment


def main():
    load_dotenv()
    bot = Bot()

    parser = argparse.ArgumentParser()
    parser.add_argument("echo")
    args = parser.parse_args()
    url_post_istagram = args.echo

    instagram_login = os.getenv("INTGRAM_LOGIN")
    instagram_passwd = os.getenv("INTGRAM_PASSWD")
    bot.login(username=instagram_login, password=instagram_passwd)

    media_id = bot.get_media_id_from_link(url_post_istagram)

    users_like = bot.get_media_likers(media_id)

    id_user_start_post = bot.get_user_id_from_username("alinavelnikovskaya")
    users_followers = bot.get_user_followers(id_user_start_post)


    if not users_followers :
        print("Список подписчиков Пустой  =  Все остановили ")
        return

    who_invited_a_friend_count = 0
    all_comments = bot.get_media_comments_all(media_id, True)
    candidates_prize = set()
    for current_comment in all_comments:
        current_user_and_usercomment = get_all_users_from_one_comment(current_comment)
        if len(current_user_and_usercomment) < 2:
            continue
        current_user = current_user_and_usercomment[0]
        current_user_str = str(current_user)
        who_invited_a_friend_count = who_invited_a_friend_count + 1
        print("{1} {0}".format(current_user_str, who_invited_a_friend_count))
        id_curent_user_int = bot.get_user_id_from_username(current_user)
        if id_curent_user_int is None:
            continue
        id_curent_user_str = str(id_curent_user_int)

        if id_curent_user_str in users_followers and  id_curent_user_str in users_like :
            candidates_prize.add(current_user)

    if not candidates_prize :
        print("Список пользователей по всем условиям Пустой !!!")
        return

    print("Список Пользователей кто выполнил все условия конкурса Instagram")
    pprint(candidates_prize)


if __name__ == '__main__':
    main()