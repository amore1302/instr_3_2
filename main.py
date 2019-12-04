from instabot import Bot
from dotenv import load_dotenv
from pprint import pprint
import argparse
import re
import os



def is_user_exist(current_user):
    if bot.get_user_id_from_username(current_user) != None:
        return True
    return False


def get_all_users_from_one_coment(current_comment):
    reg_expr_for_user_instagram = "(?:@)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)"
    resultat_list = []
    users_current_coment = re.findall(reg_expr_for_user_instagram, current_comment)
    for current_user in users_current_coment:
        if is_user_exist(current_user):
            if not (current_user in resultat_list):
                resultat_list.append(current_user)
    return resultat_list


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("echo")
    args = parser.parse_args()
    url_post_istagram = args.echo
    print(url_post_istagram)


    inst_login = os.getenv("INTGR_LOGIN")
    inst_passwd = os.getenv("INTGR_PASSWD")
    bot.login(username=inst_login, password=inst_passwd)

    media_id = bot.get_media_id_from_link(url_post_istagram)

    users_like = bot.get_media_likers(media_id)

    id_user_start_post = bot.get_user_id_from_username("alinavelnikovskaya")
    users_followers = bot.get_user_followers(id_user_start_post)


    if len(users_like) <= 0:
        print("Список подписчиков Пустой  =  Все остановили ")
        return

    ind1 = 0
    all_coments = bot.get_media_comments_all(media_id, True)
    set_who_commented = set()
    for current_coment in all_coments:
        current_user_and_usercomment = get_all_users_from_one_coment(current_coment)
        if len(current_user_and_usercomment) < 2:
            continue
        current_user = current_user_and_usercomment[0]
        current_user_str = str(current_user)
        ind1 = ind1 + 1
        print("{1} {0}".format(current_user_str, ind1))
        id_curent_user_int = bot.get_user_id_from_username(current_user)
        if id_curent_user_int == None:
            continue
        id_curent_user_str = str(id_curent_user_int)

        if id_curent_user_str in users_followers:
            if id_curent_user_str in users_like:
                set_who_commented.add(current_user)

    if len(set_who_commented) <= 0:
        print("Список пользователей по всем условиям Пустой !!!")
        return

    print("Список Пользователей кто выполнил все условия конкурса Instagram")
    pprint(set_who_commented)


if __name__ == '__main__':
    load_dotenv()
    inst_login = os.getenv("INTGR_LOGIN")
    inst_passwd = os.getenv("INTGR_PASSWD")
    bot = Bot()
    main()