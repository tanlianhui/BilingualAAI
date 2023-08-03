from moviepy.editor import *
from moviepy.video.fx import speedx
import glob
import re

def resample_avi(input_path, output_path, target_fps):
    clip = VideoFileClip(input_path)
    clip.write_videofile(output_path, fps = target_fps, codec = 'rawvideo')

directory_path = 'D:/LianHui/Desktop/*.avi'


avi_files = glob.glob(directory_path)

for file_path in avi_files:
    print(file_path)
    num = re.search('\d{3}(_\d)?', file_path)
    output_path = 'D:/LianHui/Desktop/' + "Eng" + str(num[0]) + ".avi"
    resample_avi(file_path, output_path, target_fps=60)