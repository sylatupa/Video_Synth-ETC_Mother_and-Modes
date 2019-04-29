# Video_Synth-ETC_Mother_and-Modes
A Video Synth developed from the Critter and Guitari ETC Video Synth

The Critter and Guitari ETC synth updated to work with Python3, tested on Python 3.7. Here are the fixes and updates:
* All print statements updated
* unicode and unichr funcitions update to str() and char()
* Many of the pygame drawing functions (like line and circle) were failing due to a float being passed, when an int was expected. These floats were converted in ints.

Additonal Patches were created, including:
* An L-system implementation producing a Flower/Leaf.
http://www.mediafire.com/file/5rteoppprwqcb72/flowersystem.py
https://www.pygame.org/project/1755/3062

* Chaos fractal like here:  https://www.pygame.org/project/1754
* 
