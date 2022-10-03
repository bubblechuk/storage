from pytube import YouTube
import os
import telebot
bot=telebot.TeleBot('5591356432:AAEMi2Wre6FNMi84PfFXJ07gKf4px1Q5QUs')
print('Process has been started')
a = str(input('Input Url:'))
yt=YouTube(f'{a}')
audio=yt.streams.filter(only_audio=True).get_by_itag(251)
destination = "."
out_file = audio.download(output_path=destination)
print('File is downloading...')
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
vid = open(new_file, 'rb')
bot.send_audio(1146941031, vid)
vid.close()
print('Success!')

