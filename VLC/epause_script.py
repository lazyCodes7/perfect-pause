# importing vlc module
import vlc

# importing time module
import time


# creating vlc media player object
player = vlc.MediaPlayer()

# media object
media = vlc.Media("/home/siddharth/Videos/friends_s01e01_720p_bluray_x264-sujaidr.mkv")

# setting media to the media player
player.set_media(media)


player.play()
time.sleep(10)

looking = int(input())
# pausing the video
while(True):
    player.play()
    time.sleep(2)
    if(looking == 0):
        while(True):
            player.set_pause(1)
            time.sleep(5)
            if(looking == 1):
                player.play()
                time.sleep(2)
                break



"""player.play()
time.sleep(60)"""
