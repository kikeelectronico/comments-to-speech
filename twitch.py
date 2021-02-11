from gtts import gTTS 
import os

twitch_server = 'irc.chat.twitch.tv'
twitch_port = 6667
twitch_nickname = os.environ['TWITCH_NICKNAME']
twitch_token = os.environ['TWITCH_TOKEN']
twitch_channel = os.environ['TWITCH_CHANNEL']

import socket
twitch = socket.socket()

def speech(text):
    t2s = gTTS(text=text, lang='es', slow=False) 
    t2s.save("twitch.mp3") 
    os.system("mpg321 --stereo twitch.mp3")

if __name__ == '__main__':
    twitch.connect((twitch_server, twitch_port))
    twitch.send(f"PASS {twitch_token}\n".encode('utf-8'))
    twitch.send(f"NICK {twitch_nickname}\n".encode('utf-8'))
    twitch.send(f"JOIN {twitch_channel}\n".encode('utf-8'))
    twitch.recv(2048).decode('utf-8').split('\n')
    while True:
        for comment in twitch.recv(2048).decode('utf-8').split('\n'):
            if 'PRIVMSG' in comment:
                name = comment.split(':')[1].split('!')[0]
                message = comment.split('PRIVMSG')[1].split(':')[1][0:-1]
                speech(name + ' dice ' + message + ' desde Twitch')
                print(name + ' dice ' + message + ' desde Twitch')

