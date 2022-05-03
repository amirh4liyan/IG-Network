#!/usr/bin/python3

import sys
from instagrapi import Client

KEYS = [
    "username", "full_name", "is_private", "profile_pic_url", "is_verified", "media_count",
    "follower_count", "following_count", "biography", "external_url", "is_business", "public_email",
    "contact_phone_number", "business_contact_method", "business_category_name", "category_name"
]


def utid(username):
    return cl.user_id_from_username(username)

def idtu(userID):
    return cl.username_from_user_id(userID)

def parse_by_space(text, key):
    # avoid from error of "out of range"
    text = text+" "
    value = "-1"
    if key in text:
        a = text.find(f" {key}=") + len(f" {key}=")
        b = len(text[:a]) + text[a:].find(" ")
        value = text[a:b].strip("'")
    return value

def get_following(userID):
    users = set()
    data = list(cl.user_following(userID).values())
    for case in data:
        user = parse_by_space(str(case), KEYS[0])
        users.add(user)
    return users


User = "mehrane._.mbagheri"
Pass = "div7lkmn"
cl = Client()
cl.login(User, Pass)

#target = utid(sys.argv[1])
target = utid(input('[i-str]: '))
following = get_following(target)

for user in following:
    print(user)
