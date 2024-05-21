# Changingtec mattermost bot

This is a Python bot for interacting with the Mattermost chat platform. Currently, the bot has the functionality to push
messages to specified channels and users.

## Features

- [ ] chat bot - contact info
- [ ] chat bot - the status of meeing rooms
- [ ] chat bot - Error code
- [ ] chat bot - the status of leave
- [x] notification - push message to the channel
- [x] notification - push message to the user

## Installation

1. Make sure you have Python 3.6 or higher installed. (Python 3.8 is recommended)
2. Clone the repository. recommended to use SSH.

    ```bash
    git clone git@gitlab.intranet:cglab/mtm_bot.git
    ```

3. Install the required packages.

    ```bash
    pip install -r requirements.txt
    ```

4. Set the environment variables.

    ```bash
    export MATTERMOST_TOKEN="the token of the bot"
    ```

## Usage

### Push a message to a channel.

To push messages to a specified channel, use the following function:

```python
def push_msg_channel(message: str, channel_id: str)
```

* `message`: The message to be sent.
* `channel_id`: The ID of the channel to which the message will be sent.

Example:
Push the message "Hello, world!" to the MTM test channel with the ID "ynm61k6j4f8imrfar35f1dpiqh".

```python
push_msg_channel("Hello, world!", "ynm61k6j4f8imrfar35f1dpiqh")
```

You can find the channel ID by viewing the channel information in Mattermost.

### Push a message to a user.

To push messages to a specified user, use the following function:

```python
def push_msg_user(message: str, user_name: str = None, user_id: str = None)
```

* `message`: The content of the message to be pushed.
* `user_name`: The username of the target user (optional).
* `user_id`: The ID of the target user (optional).

You must provide either user_name or user_id. If user_name is provided, the bot will attempt to find the user's ID by
their username. If the user is not found, a ValueError will be raised.

Example:

Push the message "Hello, world!" to the user with the username "codingman".

```python
push_msg_user("Hello, world!", user_name="codingman")
```

## Configuration

The bot can be configured by modifying the `config.py` file. The following parameters can be set:

* `MATTERMOST_URL`: The URL of the Mattermost server.
* `MATTERMOST_TOKEN`: The token of the bot.
* `MATTERMOST_PORT`: The port of the Mattermost server.
* `MATTERMOST_VERIFY_SSL`: Whether to verify the SSL certificate of the Mattermost server.

## Notes

* Before using the bot, make sure you have created an account in Mattermost and obtained the corresponding API token.
* The bot currently only supports the functionality of pushing messages. Additional features, such as handling chatbot
  interactions, may be added in the future.
* If you encounter any issues while using the bot, please check your configuration and ensure that your Mattermost
  account has sufficient permissions.

## Contributing

Feel free to open issues and suggestions, and submit pull requests to improve this bot.
