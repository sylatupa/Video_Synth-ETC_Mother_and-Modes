import sys
import liblo

etc = None 
osc_server = None
osc_target = None

cc_last = [0] * 5
pgm_last = 0
notes_last = [0] * 128
clk_last = 0

# OSC callbacks
def fallback(path, args):
    print("fallback",path , ' ' , args)
    pass

def fs_callback(path, args):
    global etc
    v = args
    if (v[0] > 0):
        etc.foot_pressed()

def mblob_callback(path, args):
    global etc, cc_last, pgm_last, notes_last, clk_last
    midi_blob = args[0]
    
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

def set_callback(path, args):
    global etc
    name = args[0]
    etc.set_mode_by_name(name)
    print("set patch to: " + str(etc.mode) + " with index " + str(etc.mode_index))
 
def new_callback(path, args):
    global etc
    name = args[0]
    etc.load_new_mode(name)
   
def reload_callback(path, args):
    global etc
    print("reloading: " + str(etc.mode))
    etc.reload_mode()

def knobs_callback(path, args):
    #print(path)
    print(args)
    global etc
    k1, k2, k3, k4, k5, k6 = args
    #print "received message: " + str(args)
    if k4 != -1:
        etc.knob_hardware[0] = float(k4) / 1023
    if k1 != -1:
        etc.knob_hardware[1] = float(k1) / 1023
    if k2 != -1:
        etc.knob_hardware[2] = float(k2) / 1023
    if k5 != -1:
        etc.knob_hardware[3] = float(k5) / 1023
    if k3 != -1:
        etc.knob_hardware[4] = float(k3) / 1023

def keys_callback(path, args) :
    #print(path)
    #print(args)
    global etc
    k, v = args
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

def init (etc_object) :
    global osc_server, osc_target, etc
    etc = etc_object
    
    # OSC init server and client
    try:
        osc_target = liblo.Address(4001)
    except liblo.AddressError as err:
        print("ERROR!" + err)
        sys.exit()

    try:
        osc_server = liblo.Server(4000)

        print('OOOOOOOOOOOOOOOOO    OSC 0000000000 ')
    except liblo.ServerError as err:
        print("ERROR!")
        print(str(err))
        sys.exit()

    osc_server.add_method("/knobs", 'iiiiii', knobs_callback)
    osc_server.add_method("/key", 'ii', keys_callback)
    osc_server.add_method("/mblob", 'b', mblob_callback)
    osc_server.add_method("/reload", 'i', reload_callback)
  #  osc_server.add_method("/new", 's', reload_callback)
    osc_server.add_method("/set", 's', set_callback)
    osc_server.add_method("/new", 's', new_callback)
    osc_server.add_method("/fs", 'i', fs_callback)
    osc_server.add_method(None, None, fallback)

def recv() :
    global osc_server
    while (osc_server.recv(1)):
        pass

def send(addr, args) :
    global osc_target
    liblo.send(osc_target, addr, args) 
