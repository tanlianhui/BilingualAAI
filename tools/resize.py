### AVI files ###
from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx
import glob
import re

def resize(input_path, output_path):
    clip = VideoFileClip(input_path)
    new_clip = clip.resize((320,240))
    new_clip.write_videofile(output_path, codec="rawvideo")


directory_path = 'E:/*.avi'
avi_files = glob.glob(directory_path)

for file_path in avi_files:
    print(file_path)
    num = re.search('\d{3}(_\d)?', file_path)
    output_path = 'E:/' + "Eng" + str(num[0]) + ".avi"
    resize(file_path, output_path)
