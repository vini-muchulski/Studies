from moviepy.editor import *
#from moviepy.editor import vfx,VideoFileClip,concatenate_videoclips
#https://www.youtube.com/watch?v=t2EFj25tGRQ

clip1 = VideoFileClip("ironman.mp4").subclip(100,110).fx(vfx.fadeout,0.5 )
clip2 = VideoFileClip("ironman.mp4").subclip(118,158).fx(vfx.fadein,0.5 ).fx(vfx.fadeout,1 )

video_final = concatenate_videoclips([clip1,clip2])
video_final.write_videofile("ironman_vs_f22.mp4")

