#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Beat tracking example

import librosa
import os
from scipy.interpolate import interp1d

# 1. Generic variables TODO: make them input parameters



# Assuming that into "video_input_file_frame" U've already extracted original video frames
# with "ffmpeg -i input.mp4 %04d.png"



# in doing that  keep track of orignal video's FPS (30 or 60 or antani)
# use FPS to set
video_input_fps = 30

# Check size of single frames Ex: 1280 x 720 and set the corresponding output varaibles
v_h = 1280
v_w = 720


# Assuming that into "generated" directoruy U've already create "project_name" subfolder
project_name = 'bici'
audio_input_file = '/home/lalo/data/studio_suono/Targa/T0-210909-1111.wav'
working_dir = '/home/lalo/data/studio_grafica/warp_diffusion/' + project_name + "/"
input_dir = working_dir + 'input/'
output_dir = working_dir + 'output/'


#    Store the sampling rate as `sr`

y, sr = librosa.load(audio_input_file)
rms = librosa.feature.rms(y=y, frame_length=735, hop_length=735)
m = interp1d([rms.min(), rms.max()], [100, 200])


# Creating the sctipt file (the real unique aoutput of this script)
try:
    f = open(working_dir + "/" + project_name + ".sh", "w")
    ext = ('png')
    # iterating over all files


    for frame in sorted(os.listdir(input_dir)):
        if frame.endswith(ext):
            #magick 0001.png  -modulate 100 0001_modulate_2.png
            print('Processing frame:  ' + frame)
            zero = int(frame[0:4])
            f.write("magick " + input_dir + frame + "  -modulate " + str(int(m(rms[0][int(frame[0:4])]))) + " "  +output_dir + frame + "\n")
        else:
            continue
except:
    f.close()



#audio frame size is 22050/30=735



# 3. Run the default beat tracker

