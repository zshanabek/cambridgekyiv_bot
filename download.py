import youtube_dl


options = {
  'format': 'bestaudio/best',
  'extractaudio' : True,
  'audioformat' : "mp3",
  'outtmpl': '%(id)s',
  'noplaylist' : True
}

def		get_video_info(url)
	r = None
	ydl = youtube_dl.YoutubeDL(options)
	with ydl:
		r = ydl.extract_info(url, download=False)  