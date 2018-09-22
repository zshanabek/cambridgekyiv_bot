import youtube_dl
import traceback
import pdb
import os


def		get_video_info(url):
	ydl = youtube_dl.YoutubeDL()
	try:
		with ydl:
			r = ydl.extract_info(url, download=False)
		return 1
	except Exception as e:
		return None

def		get_audio(url):
	options = {
		'format': 'bestaudio/best', # choice of quality
		'extractaudio' : True,      # only keep the audio
		'audioformat' : "mp3",      # convert to mp3 
		'outtmpl': '%(id)s',        # name the file the ID of the video
		'noplaylist' : True
	}
	ydl = youtube_dl.YoutubeDL(options)
	try:
		result = ydl.extract_info(url, download=True)
		os.rename(result['id'], "{}.mp3".format(result['title']))
		return result['title']
	except Exception as e:
		return None