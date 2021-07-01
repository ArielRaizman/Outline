import json
import numpy as np

from moviepy.editor import *
from moviepy.video.tools.drawing import circle
from moviepy.video.tools.cuts import find_video_period
from moviepy.video.tools.segmenting import findObjects


f = open('C:\\Users\\ariel\\Downloads\\testDeceptorJSON.json')

data = json.load(f) #violations

# print(data['violations']['ACR-007'])

acrList = []

for i in data['violations']:
    print(data['violations'][i])
    acrList.append(i)

print(acrList)






clip = ImageClip("C:\\Users\\ariel\\Downloads\\white.png").set_duration(15)
clip.size = (1920,1080)
w,h = clip.size
print(clip.size)
textbox = ImageClip("C:\\Users\\ariel\\Downloads\\bluebox.png").set_duration(clip.duration)
violation = ImageClip("C:\\Users\\ariel\\Downloads\\violation.png").set_duration(clip.duration).fx( vfx.resize, width=1250)
blur = ImageClip("C:\\Users\\ariel\\Downloads\\blur.PNG").set_duration(clip.duration).fx( vfx.resize, width=300)
acr = TextClip(str(acrList[0]),None, None, 'orange','transparent',81,'Comic-Sans-MS').set_duration(clip.duration)


moviesize = w,h
txt = "\n".join([
"A long time ago, in a faraway galaxy,",
"there lived a prince and a princess",
"who had never seen the stars, for they",
"lived deep underground.",
"",
"Many years before, the prince's",
"grandfather had ventured out to the",
"surface and had been burnt to ashes by",
"solar winds.",
"",
"One day, as the princess was coding",
"and the prince was shopping online, a",
"meteor landed just a few megameters",
"from the couple's flat."
])


# Add blanks
txt = 10*"\n" +txt + 10*"\n"

clip_txt = TextClip(txt,color='orange', align='West',fontsize=25, font='Xolonium-Bold', method='label').set_duration(clip.duration)

txt_speed = 27
fl = lambda gf,t : gf(t)[int(txt_speed*t):int(txt_speed*t)+h,:]
moving_txt= clip_txt.fl(fl, apply_to=['mask'])










final = CompositeVideoClip([
                            clip,
                            textbox.set_pos([int(0.02*w),int(0.02*h)]),
                            blur.set_pos([int(0.05*w),int(0.7*h)]),
                            violation.set_pos([int(0.3*w),int(0.1*h)]),
                            moving_txt.set_pos(('center','bottom')), #lambda t:(40t,'center')  the_end.set_pos(lambda t:('center',0+40*t)) [int(0.2*w),int(0.2*h)]
                            acr.set_pos([int(0.37*w),int(0.11*h)])],
                           size =clip.size)



final.write_videofile("C:\\Users\\ariel\\Downloads\\oopoop.mp4", fps = 60, codec="libx264")