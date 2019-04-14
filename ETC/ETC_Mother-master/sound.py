try:
    import alsaaudio, audioop
except:
    pass
import pyaudio,wave, audioop

import time
import math

inp = None
etc = None
trig_this_time = 0
trig_last_time = 0
sin = [0] * 100

FORMAT = pyaudio.paInt16
CHANNELS = 2
CHANNELS = 1 # 4/1/2019
RATE = 44100 # this was orignal but was making the wrong number of frames for the loop below 
RATE = 11025   #settled on this going to increase th frame rate
#RATE = 8000  #4/1/2019 change seen on github
CHUNK = 1024
CHUNK = 1024
CHUNK = 1024
RECORD_SECONDS = 5
audio = pyaudio.PyAudio()
 
def callback(in_data, frame_count, time_info, status):
    global inp, etc, trig_this_time, trig_last_time, sin
    data = in_data
    peak=0
    try :
        #print('range', int(RATE / CHUNK * RECORD_SECONDS))
        #print('data',len(data))
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            avg = audioop.getsample(data, 2, i * 3)
            avg += audioop.getsample(data, 2, (i * 3) + 1)
            avg += audioop.getsample(data, 2, (i * 3) + 2)
            avg = avg / 3
            if (avg > 1000) :
                trig_this_time = time.time()
                a =trig_this_time# - trig_last_time
                #print(a)
                #print(avg)
                if (trig_this_time - trig_last_time) > .05:
                    etc.audio_trig = True
                    trig_last_time = trig_this_time

                if avg > peak :
                    etc.audio_peak = avg
                    peak = avg
                # if the trigger button is held
                #print(etc.trig_button)
                if (etc.trig_button) :
                    etc.audio_in[i] = sin[i] 
                else :
                    #print(etc.audio_in)
                    #print(len(etc.audio_in))
                    #print(i)
                    etc.audio_in[i] = avg
    except Exception as e:
        print('ERROR!!!  ', e)
        pass
    return (data, pyaudio.paContinue)
#stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK,stream_callback=callback)

# open stream using callback (3)
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK,stream_callback=callback)

stream.start_stream()

for i in range(0,100) :
    sin[i] = int(math.sin(2 * 3.1459 * i / 100) * 32700)
def init (etc_object) :
    global inp, etc, trig_this_time, trig_last_time, sin
    etc = etc_object
    #setup alsa for sound in
    """
    inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)

    inp.setchannels(1)
    inp.setrate(8000)
    inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    inp.setperiodsize(300)
    trig_last_time = time.time()
    trig_this_time = time.time()
    """
    for i in range(0,100) :
        sin[i] = int(math.sin(2 * 3.1459 * i / 100) * 32700)

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)        

def initA (etc_object) :
    global inp, etc, trig_this_time, trig_last_time, sin
    etc = etc_object    
 
    # start Recording

def recv() :
    global inp, etc, trig_this_time, trig_last_time, sin
    # get audio
    #l,data = inp.read()
    peak = 0
    while 1:
        
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

            try :
                avg = audioop.getsample(data, 2, i * 3)
                avg += audioop.getsample(data, 2, (i * 3) + 1)
                avg += audioop.getsample(data, 2, (i * 3) + 2)
                avg = avg / 3
                if (avg > 20000) :
                    trig_this_time = time.time()
                    if (trig_this_time - trig_last_time) > .05:
                        etc.audio_trig = True
                        trig_last_time = trig_this_time

                if avg > peak :
                    etc.audio_peak = avg
                    peak = avg
                # if the trigger button is held
                if (etc.trig_button) :
                    etc.audio_in[i] = sin[i] 
                else :
                    etc.audio_in[i] = avg

            except :
                pass
        #l,data = inp.read()
"""
        for i in range(0,100) :
            try :
                avg = audioop.getsample(data, 2, i * 3)
                avg += audioop.getsample(data, 2, (i * 3) + 1)
                avg += audioop.getsample(data, 2, (i * 3) + 2)
                avg = avg / 3
                if (avg > 20000) :
                    trig_this_time = time.time()
                    if (trig_this_time - trig_last_time) > .05:
                        etc.audio_trig = True
                        trig_last_time = trig_this_time
                if avg > peak :
                    etc.audio_peak = avg
                    peak = avg
                # if the trigger button is held
                if (etc.trig_button) :
                    etc.audio_in[i] = sin[i] 
                else :
                    etc.audio_in[i] = avg

            except :
                pass
        l,data = inp.read()

"""
frames = []
 
#for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#        data = stream.read(CHUNK)
#    frames.append(data)

# stop Recording
#stream.stop_stream()
#stream.close()
#audio.terminate()

def recva() :
    global inp, etc, trig_this_time, trig_last_time, sin
    # get audio
    #l,data = inp.read()
    peak = 0

    stream.start_stream()
    while stream.is_active():
        time.sleep(.4)

   # for 
    stream.stop_stream()
        #l,data = inp.read() 

