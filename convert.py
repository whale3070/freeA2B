from moviepy.editor import *

def convert_avi_to_mp4(avi_file, mp4_file):
    video = VideoFileClip(avi_file)
    video.write_videofile(mp4_file, codec="libx264")

# 示例用法
avi_file = "input.avi"
mp4_file = "output.mp4"

convert_avi_to_mp4(avi_file, mp4_file)
