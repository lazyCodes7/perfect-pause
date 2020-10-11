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
value = media_player.get_length()
print(value)
# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(5)

# pausing the video
media_player.set_pause(1)
time.sleep(5)
media_player.play()
time.sleep(60)
