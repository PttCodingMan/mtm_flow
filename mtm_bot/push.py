import os
from typing import Optional

from mattermostautodriver import Driver

driver: Optional[Driver] = None

cache = {}


def _login():
    global driver

    driver = Driver(
        options=
        {
            "url": os.getenv("MATTERMOST_HOST"),
            "token": os.getenv("MATTERMOST_TOKEN"),
            "port": int(os.getenv("MATTERMOST_PORT")),
            "verify": os.getenv("MATTERMOST_VERIFY_SSL").lower == "true"
        })
    driver.login()


def _logout():
    global driver

    if driver is not None:
        driver.logout()
        driver = None


def push_msg_channel(message: str, channel_id: Optional[str] = None):
    if driver is None:
        _login()

    if channel_id is not None:
        pass
    else:
        raise ValueError("channel_id must be provided.")

    driver.posts.create_post(
        options={
            'channel_id': channel_id,
            'message': message
        })


def push_msg_user(message: str,
                  user_name: Optional[str] = None,
                  user_id: Optional[str] = None,
                  user_mail: Optional[str] = None):
    if driver is None:
        _login()

    if user_id is not None:
        pass
    elif user_name is not None or user_mail is not None:

        if user_name in cache:
            user_id = cache[user_name]
        elif user_mail in cache:
            user_id = cache[user_mail]
        else:

            if user_name is not None:
                user_id = driver.users.get_user_by_username(user_name)['id']
            elif user_mail is not None:
                user_id = driver.users.get_user_by_email(user_mail)['id']

            if user_id is None:
                raise ValueError(f"User '{user_name}' not found.")

            cache[user_name] = user_id
    else:
        raise ValueError("Either user_name or user_id must be provided.")

    direct_channel_id = driver.channels.create_direct_channel([
        driver.client.userid,
        user_id
    ])['id']

    push_msg_channel(message, channel_id=direct_channel_id)
