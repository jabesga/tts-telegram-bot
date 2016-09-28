from bot import Bot
from gtts import gTTS
import os
import subprocess

TOKEN = '#####BOTOKEN####'
bot = Bot(TOKEN)

while True:
    try:
        json_response = bot.process_updates()
        if json_response:
            if 'message' in json_response:
                if 'text' in json_response['message']:
                    text = 'De {}, {}'.format(json_response['message']['from']['first_name'], json_response['message']['text'])
                    print(text)
                    tss = gTTS(text=text, lang='es')
                    tss.save('sound.mp3')
                    response = subprocess.call("./raspberry_audio.sh", shell=True)
                    print(response)
    except requests.exceptions.RequestException:
        pass
