from instabot import Bot
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

    mentions = re.findall(reg_expr_for_user_instagram, current_comment)
    filtered_mentions = {mention for mention in mentions if is_user_exist(user)}
    return filtered_mentions
	

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

    like_users = bot.get_media_likers(media_id)

    start_post_user_id = bot.get_user_id_from_username("alinavelnikovskaya")
    followers_users = bot.get_user_followers(start_post_user_id)


    if not followers_users :
        print("Список подписчиков Пустой  =  Все остановили ")
        return

    who_invited_a_friend_count = 0
    all_comments = bot.get_media_comments_all(media_id, True)
    prize_candidates = set()
    for current_comment in all_comments:
        current_user_and_usercomment = get_all_users_from_one_comment(current_comment)
        if len(current_user_and_usercomment) < 2:
            continue
        current_user = current_user_and_usercomment[0]
        who_invited_a_friend_count = who_invited_a_friend_count + 1
        print("{1} {0}".format(current_user_str, who_invited_a_friend_count))
        id_current_user_int = bot.get_user_id_from_username(current_user)
        if id_current_user_int is None:
            continue
        id_curtent_user_str = str(id_current_user_int)

        if id_curtent_user_str in followers_users and  id_curtent_user_str in like_users :
            prize_candidates.add(current_user)

    if not prize_candidates :
        print("Список пользователей по всем условиям Пустой !!!")
        return

    print("Список Пользователей кто выполнил все условия конкурса Instagram")
    pprint(prize_candidates)


if __name__ == '__main__':
    main()