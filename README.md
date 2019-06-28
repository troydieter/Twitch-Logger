# Twitch Logger
Log the Twitch chats of your favorite channels and convert them into data frames for analysis.

## Installation
 1. Download or clone this repository and navigate to the directory
 ```
    git clone https://github.com/melsantos/Twitch-Logger/
 ```
 2. Install the required packages using pip
 ```
    pip install -r requirements.txt
 ```

## Usage
 1. Navigate to the directory
 2. Open the `.env` file and edit the following
    + `TWITCH_OAUTH_TOKEN`: Insert your Twitch OAuth Token which you can get [here](https://twitchapps.com/tmi/).
    + `NICKNAME`: Twitch account name associated with your Twitch OAuth Token.
    + `CHANNEL`: Name of the Twitch channel whose chats you want to start logging.
 3. Run `python get_chat_log.py` and you should be greeted with a welcome message from Twitch.
 ```
$ python get_chat_log.py
    :tmi.twitch.tv 001 TWITCH_NAME :Welcome, GLHF!
    :tmi.twitch.tv 002 TWITCH_NAME :Your host is tmi.twitch.tv
    :tmi.twitch.tv 003 TWITCH_NAME :This server is rather new
    :tmi.twitch.tv 004 TWITCH_NAME :-
    :tmi.twitch.tv 375 TWITCH_NAME :-
    :tmi.twitch.tv 372 TWITCH_NAME :You are in a maze of twisty passages, all alike.
    :tmi.twitch.tv 376 TWITCH_NAME :>

    :TWITCH_NAME!TWITCH_NAME@TWITCH_NAME.tmi.twitch.tv JOIN #CHANNEL_NAME
    :TWITCH_NAME.tmi.twitch.tv 353 TWITCH_NAME = #CHANNEL_NAME :TWITCH_NAME
    :TWITCH_NAME.tmi.twitch.tv 366 TWITCH_NAME #CHANNEL_NAME :End of /NAMES list
 ```
The Twitch chat should start outputting to the terminal. The chat logs will be stored in `channel_logs/CHANNEL_NAME/MM-DD HH-mm.log`.


## Future Improvements / Known Issues
 + Make a terminal based interface
 + Does not log messages from chat alerts
 + Create script to generate most used emotes

## Credits
 + [How to Stream Text Data from Twitch with Sockets in Python](https://www.learndatasci.com/tutorials/how-stream-text-data-twitch-sockets-python/) - A lot of this code is from this tutorial.

