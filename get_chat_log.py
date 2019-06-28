from datetime import datetime
from decouple import config
from emoji import demojize
import socket, logging, re, os, errno

# define constants
server = 'irc.chat.twitch.tv'
port = 6667
nickname = config('NICKNAME')
token = config('TWITCH_OAUTH_TOKEN')
channel = config('CHANNEL')

now = datetime.now()

# Create socket
sock = socket.socket()
sock.connect((server, port))

# Log into twitch and join channel
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

# code taken from https://stackoverflow.com/a/12517490 to create separate channel directories
filedir = 'channel_logs/%s/' % (channel[1:]) 
if not os.path.exists(os.path.dirname(filedir)):
    try:
        os.makedirs(os.path.dirname(filedir))
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise

# define logging format
filepath = filedir + '%s chat.log' % (now.strftime("%m-%d %H-%M"))
logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s = %(message)s',
                        datefmt='%Y-%m-%d_%H:%M:%S',
                        handlers=[logging.FileHandler(filepath, encoding='utf-8')])

# write to log continously
while True:
    msg = sock.recv(2048).decode('utf-8')
    print(demojize(msg))

    if msg.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))
    elif len(msg) > 0:
        logging.info(demojize(msg))
        pass

sock.close()
