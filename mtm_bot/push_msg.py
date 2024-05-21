import os

import push

if __name__ == '__main__':

    message = os.environ.get("MATTERMOST_MESSAGE")
    if message is None:
        raise ValueError("MATTERMOST_MESSAGE must be provided.")

    channel_id = os.environ.get("MATTERMOST_CHANNEL_ID")

    user_name = os.environ.get("MATTERMOST_USER_NAME")
    user_mail = os.environ.get("MATTERMOST_USER_MAIL")

    if channel_id is not None:
        push.push_msg_channel(message, channel_id=channel_id)

    if user_name is None and user_mail is not None:
        push.push_msg_user(message, user_mail=user_mail)

    if user_name is not None:
        push.push_msg_user(message, user_name=user_name)
