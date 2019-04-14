import pygame
import pygame.midi
from pygame.locals import *

midi_input = None
etc = None
cc_last = [0] * 5
pgm_last = 0

def parse_midi(midi):
    global etc, cc_last, pgm_last

    for msg in midi:
        midi_msg = msg[0]
        #print(midi_msg)
        msg_status = int(midi_msg[0])
        msg_channel = msg_status & 0xf
        msg_type = (msg_status >> 4) & 0xf
   
        # global message clock tick
        if (msg_status == 248) :
            etc.new_midi = True
            etc.midi_clk += 1
            if (etc.midi_clk >= 24) : etc.midi_clk = 0

        # global message clock start
        if (msg_status == 250) :
            etc.new_midi = True
            etc.midi_clk = 0

        # channel messages
        if ( (msg_channel == (etc.midi_ch - 1)) or (etc.midi_ch == 0)) :
            
            print('ChannelMessage',msg_channel, ' etc_midi_ch',etc.midi_ch)
            # CC
            if (msg_type == 0xB) :
                print('msg_type',msg_type)
                etc.new_midi = True
                for i in range(0,5) :
                    if (midi_msg[1] == 21 + i) :
                        cc = midi_msg[2]
                        if cc != cc_last[i] :
                            etc.cc_override_knob(i, float(cc) / 127)
                            cc_last[i] = cc
 
            # note OFF
            if (msg_type == 0x8) :
                print('noteOff',msg_type)
                etc.new_midi = True
                etc.midi_notes[midi_msg[1]] = 0

            # note ON
            if (msg_type == 0x9) :
                print('noteOn',msg_type)
                etc.new_midi = True
                print(midi_msg[1])
                if (midi_msg[1] == 1 and midi_msg[2]==0) :
                    etc.next_mode()
                if (midi_msg[1] == 2 and midi_msg[2]==0) :
                    etc.prev_mode()
                if (midi_msg[1] == 3 and midi_msg[2]==0) :
                    etc.update_trig_button(v)
                if (midi_msg[1] == 4 and midi_msg[2]==0) :
                    etc.prev_scene()
                if (midi_msg[1] == 5 and midi_msg[2]==0) :
                    etc.save_or_delete_scene(v)                    
                if (midi_msg[1] == 6 and midi_msg[2]==0) :                
                    etc.next_scene()
                
                else :
                    etc.midi_notes[midi_msg[1]] = 0
                #if (midi_msg[2] > 0) :
                #if (midi_msg[2] > 0) :
                #if (midi_msg[2] > 0) :
               
               
                #if (midi_msg[2] > 0) :
                #     etc.midi_notes[midi_msg[1]] = 1
                
#etc.prev_scene()
#etc.save_or_delete_scene(v)
#etc.next_scene()
            # PGM
            if (msg_type == 0xC) :
                print('msg_type PGM',msg_type)
                etc.new_midi = True
                pgm = midi_msg[1]
                if (pgm != pgm_last):
                    etc.midi_pgm = pgm
                    pgm_last = pgm


def _print_device_info():
    for i in range( pygame.midi.get_count() ):
        r = pygame.midi.get_device_info(i)
        (interf, name, input, output, opened) = r

        in_out = ""
        if input:
            in_out = "(input)"
        if output:
            in_out = "(output)"

        etc.usb_midi_name = name
    
        print ("%2i: interface :%s:, name :%s:, opened :%s:  %s" %
               (i, interf, name, opened, in_out))


def init(etc_obj) :
    global etc, midi_input
    etc = etc_obj

    pygame.midi.init()
    print(pygame.midi.get_device_info(20))
    print(pygame.midi.get_device_info(20))
    print(pygame.midi.get_device_info(20))
    try :
        _print_device_info()
        print('input: '+ pygame.midi.Input)
        input_id = pygame.midi.get_default_input_id()

        print ("using input_id :%s:" % input_id)
        midi_input = pygame.midi.Input( input_id )
        etc.usb_midi_present = True
    except :
        print("no usb midi found")
        etc.usb_midi_present = False

def poll():
    global midi_input
    if (etc.usb_midi_present ) :
        if midi_input.poll():
            midi_events = midi_input.read(100)
            #knobs_callback()
            #keys_callback()
            '''
            mblob_callback()
            reload_callback()
 
            set_callback()
            New_callback()
            fs_callback()
            fallback()
            '''

            try :
                parse_midi(midi_events)
            except :
                print("problem with usb midi")


def fallback(path, args):
    pass

def fs_callback(path, args):
    global etc
    v = args
    if (v[0] > 0):
        etc.foot_pressed()

def mblob_callback(path, args):
    global etc, cc_last, pgm_last, notes_last, clk_last
    midi_blob = args[0]
    #print(midi_blob)
    for i in range(0, 5) :
        cc = midi_blob[16 + i]
        if cc != cc_last[i] :
            etc.cc_override_knob(i, float(cc) / 127)
            cc_last[i] = cc
            
    clk = midi_blob[21]
    if (clk != clk_last):
        etc.midi_clk = midi_blob[21]
        clk_last = clk

    pgm = midi_blob[22]
    if (pgm != pgm_last):
        etc.midi_pgm = pgm
        pgm_last = pgm

    # parse the notes outta the bit field
    for i in range(0, 16) :
        for j in range(0, 8) :
            if midi_blob[i] & (1<<j) :
                if(notes_last[(i*8)+j] != 1) : 
                    etc.midi_notes[(i * 8) + j] = 1
                    notes_last[(i*8)+j] = 1
            else :
                if(notes_last[(i*8)+j] != 0) : 
                    etc.midi_notes[(i * 8) + j] = 0
                    notes_last[(i*8)+j] = 0

def set_callback():
    global etc
    name = args[0]
    etc.set_mode_by_name(name)
    print("set patch to: " + str(etc.mode) + " with index " + str(etc.mode_index))
 
def new_callback():
    global etc
    name = args[0]
    etc.load_new_mode(name)
   
def reload_callback():
    global etc
    print("reloading: " + str(etc.mode))
    etc.reload_mode()

def knobs_callback():
    global etc
    k1, k2, k3, k4, k5, k6 = args
    #print "received message: " + str(args)
    etc.knob_hardware[0] = float(k4) / 1023
    etc.knob_hardware[1] = float(k1) / 1023
    etc.knob_hardware[2] = float(k2) / 1023
    etc.knob_hardware[3] = float(k5) / 1023
    etc.knob_hardware[4] = float(k3) / 1023

def keys_callback() :
    global etc
    k, v = args
    print("midi args" + args)
    if (k == 2 and v > 0) : etc.next_mode()
    if (k == 1 and v > 0) : etc.prev_mode()
    if (k == 9) : etc.update_trig_button(v)
    if (k == 7 and v > 0) : etc.screengrab_flag = True
    if (k == 4 and v > 0) : etc.prev_scene()
    if (k == 6) : etc.save_or_delete_scene(v)
    if (k == 5 and v > 0) : etc.next_scene()
    if (k == 3 and v > 0) : 
        if (etc.osd) : etc.set_osd(False)
        else : etc.set_osd(True)
    if (k == 8 and v > 0) : 
        if (etc.auto_clear) : etc.auto_clear = False
        else : etc.auto_clear = True

