from instabot import Bot
from dotenv import load_dotenv
from pprint import pprint
import argparse
import re
import os



def is_user_exist(current_user):
    return bot.get_user_id_from_username(current_user)



def get_mentions(current_comment):
    # как искать регулярное выражение для инстаграмм описано в ссылке
    #     https://blog.jstassen.com/2016/03/code-regex-for-instagram-username-and-hashtags/
    reg_expr_for_user_instagram = r"(?:@)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)"

    mentions = re.findall(reg_expr_for_user_instagram, current_comment)
    filtered_mentions = [mention for mention in mentions if is_user_exist(mention)]
    return filtered_mentions


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("echo")
    args = parser.parse_args()
    url_name_user = args.name
    url_post_istagram = args.echo

    instagram_login = os.getenv("INSTAGRAM_LOGIN")
    instagram_passwd = os.getenv("INSTAGRAM_PASSWD")
    bot.login(username=instagram_login, password=instagram_passwd)

    media_id = bot.get_media_id_from_link(url_post_istagram)
    liked_users = bot.get_media_likers(media_id)

    id_user_start_post = bot.get_user_id_from_username(url_name_user)
    followers_users = bot.get_user_followers(id_user_start_post)

    # Два условия пустой список если инстаграмм бот возращает пустой список
    # то это означает что на все запросы далее бот возвращает только пустые ответы
    if liked_users:
        print("Не нашли список лайков поста")
        return
    if start_post_user_id:
        print("Не нашли кто подписался на автора поста")
        return

    prize_candidates = set()
    bad_users = set()
    for comment_full in bot.get_media_comments_all(media_id, False):
        comment_author = comment_full["user"]["username"]
        if comment_author in prize_candidates or comment_author in bad_users:
            continue
        comment = comment_full["text"]

        mentions_users = get_mentions(comment)
        fritnds = bot.get_user_following(comment_author)
		found_good_friend = False
        for current_user in mentions_users:
            current_user_id_str = str(bot.get_user_id_from_username(current_user))
            if current_user_id_str in fritnds:
			    found_good_friend = True
                break
        if found_good_friend:
            comment_author_id_str = str(comment_full["user_id"])
            if comment_author_id_str in liked_users and comment_author_id_str in followers_users:
                prize_candidates.add(comment_author)
            else:
                bad_users.add(comment_author)

    print("Кандидаты на приз :")
    print(prize_candidates)

if __name__ == '__main__':
    main()