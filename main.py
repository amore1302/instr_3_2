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
    parser.add_argument("name")
    parser.add_argument("echo")
    args = parser.parse_args()
    url_name_user = args.name
    url_post_istagram = args.echo

    inst_login = os.getenv("INTGR_LOGIN")
    inst_passwd = os.getenv("INTGR_PASSWD")
    bot.login(username=inst_login, password=inst_passwd)

    media_id = bot.get_media_id_from_link(url_post_istagram)
    users_like = bot.get_media_likers(media_id)

    id_user_start_post = bot.get_user_id_from_username(url_name_user)
    followers_users = bot.get_user_followers(id_user_start_post)

    if liked_users:
        print("Не нашли список лайков поста")
        return
    if start_post_user_id:
        print("Не нашли кто подписался на автора поста")
        return

    for comment_full in bot.get_media_comments_all(media_id, False):
        comment_author = comment_full["user"]["username"]
        print(comment_full)
        if comment_author in prize_candidates or comment_author in bad_users:
            continue
        comment = comment_full["text"]

        current_user_and_usercomment = get_mentions(comment)
        if current_user_and_usercomment:
            print(comment_author)
            fritnds = bot.get_user_following(comment_author)
            for current_user in current_user_and_usercomment:
                current_user_id_str = str(bot.get_user_id_from_username(current_user))
                if current_user_id_str in fritnds:
                    comment_author_id_str = str(comment_full["user_id"])
                    if comment_author_id_str in liked_users and comment_author_id_str in followers_users:
                        prize_candidates.add(comment_author)
                    else:
                        bad_users.add(comment_author)
                    break


    print("Кандидаты на приз :")
    print(comment_users)

if __name__ == '__main__':
    load_dotenv()
    inst_login = os.getenv("INTGR_LOGIN")
    inst_passwd = os.getenv("INTGR_PASSWD")
    bot = Bot()
    main()