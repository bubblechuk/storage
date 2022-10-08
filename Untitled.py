from pytube import YouTube
import os
import telebot
bot=telebot.TeleBot('5591356432:AAEMi2Wre6FNMi84PfFXJ07gKf4px1Q5QUs')
userid = int(input('Введите свой TelegramID: '))
while True:
	yt = YouTube(str(input("Введите ссылку на ваше видео: \n ")))
	video = yt.streams.filter(only_audio=True).first()
	out_file = video.download(output_path='.')
	base, ext = os.path.splitext(out_file)
	new_file = str(input('Введите название файла (по желанию): ')+'.mp3') or base+'.mp3'
	os.rename(out_file, new_file)
	print(yt.title + " был загружен.")
	ss=open(new_file, 'rb')
	bot.send_audio(userid, ss, timeout=999)
	ss.close()
	os.remove(new_file)
bot.polling(none_stop=True)
