import pygame
import mido

from mido.ports import BaseOutput

class PrintPort(BaseOutput):
    def _send(message):
        print(message)

port = PrintPort()
print(port)
while True:
    for i in range(0,127):
        for j in range(0,127):
            a = mido.Message('note_on', note=i, velocity=j, time=.5 , channel=1)   
#port.send(msg)
#note_on channel=0 note=0 velocity=64 time=0
"""
if __name__ == '__main__':
  while True:
    entered = input("Please enter your three-letter code or leave a blank line to quit: ")
    if not entered: break
    if len(entered) != 3:
      print("%r is NOT three letters, it's %d" % (entered, len(entered)))
      continue
    if not entered.isalpha():
      print("%r are NOT all letters -- please enter exactly three letters, nothing else!")
      continue
    process(entered)

"""
