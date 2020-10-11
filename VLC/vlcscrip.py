# importing vlc module
import vlc

# importing time module
import time


# creating vlc media player object
media_player = vlc.MediaPlayer()



# media object
media = vlc.Media("/home/dazedtiara6667/test/7th Grade Crush _ Brooklyn Nine-Nine.mp4")


# setting media to the media player
media_player.set_media(media)

media_player.audio_set_volume(100)
# start playing video
media_player.play()

# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(5)

value = 1
# printing value
while(value):
	media_player.set_pause(1)
	time.sleep(1)
	if(value==0):
		media_player.play()
	value=1
# pausing the video 
