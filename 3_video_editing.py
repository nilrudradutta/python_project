from moviepy.editor import *

clip1 = VideoFileClip("newnilu4.mp4").subclip(5,13)
clip2 = VideoFileClip("newnilu9.mp4").subclip(14,28)

clip2 = clip2.set_position((45,150))

final_video = concatenate_videoclips([clip1,clip2])
final_video.write_videofile("new_nilu.mp4")
#new_nilu.mp4 is the marge vdo of the newnilu4.mp4 and newnilu9.mp4