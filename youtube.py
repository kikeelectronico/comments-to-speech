from gtts import gTTS 
import os
import pytchat

youtube_id = os.environ['YOUTUBE_ID']

youtube = pytchat.create(video_id=youtube_id)

  
def speech(text):
    t2s = gTTS(text=text, lang='es', slow=False) 
    t2s.save("youtube.mp3") 
    os.system("mpg321 --stereo youtube.mp3")

if __name__ == '__main__':
    while True:
        for comment in youtube.get().sync_items():
            speech(str(comment.author.name) + ' dice ' + str(comment.message) + ' desde YouTube')
            print(str(comment.author.name) + ' dice ' + str(comment.message) + ' desde YouTube')
