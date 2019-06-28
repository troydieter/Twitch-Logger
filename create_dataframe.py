from datetime import datetime
from decouple import config
import pandas as pd
import re, os

channel = config('CHANNEL')[1:]

def get_chat_dataframe(file):
    data = []

    with open(file, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n\n\n')

        for line in lines:
            try:
                time_logged = line.split()[0].strip()
                time_logged = datetime.strptime(time_logged, '%Y-%m-%d_%H:%M:%S')

                username_message = line.split('=')[1:]
                username_message = '='.join(username_message).strip()

                username, channel, message = re.search(
                    ':(.*)!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)', username_message
                ).groups()

                d = {
                    'dt': time_logged,
                    'channel': channel,
                    'username': username,
                    'message': message,
                }

                data.append(d)
            except Exception:
                pass # just pretend nothing happened :smile: 

    return pd.DataFrame().from_records(data)

def main(): 
    cwd = os.getcwd()

    # code taken from https://stackoverflow.com/a/12517490 to create separate channel directories
    filedir = 'data_frames/%s/' % (channel) 
    if not os.path.exists(os.path.dirname(filedir)):
        try:
            os.makedirs(os.path.dirname(filedir))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    for filename in os.listdir(cwd + '\\channel_logs\\' + channel):
        df = get_chat_dataframe('channel_logs/' + channel + '/' + filename)
        df.set_index('dt', inplace=True)
        df.to_csv(filedir + '/' + channel + '_' + re.sub(' chat.log', '', filename) + '.csv')
        print(df.shape)
        df.head()

if __name__ == '__main__':
    main()