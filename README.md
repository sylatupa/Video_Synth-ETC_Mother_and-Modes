# Video_Synth-ETC_Mother_and-Modes
A Video Synth developed from the Critter and Guitari ETC Video Synth

## The Critter and Guitari ETC synth updated to work with Python3, tested on Python 3.7. Here are the fixes and updates:
* All print statements updated
* unicode and unichr funcitions update to str() and char()
* Many of the pygame drawing functions (like line and circle) were failing due to a float being passed, when an int was expected. These floats were converted in ints.

![pop_chaos]

# Additonal Patches were created, including:
* [S - A1_AFlower_Sauce](https://github.com/sylatupa/Video_Synth-ETC_Mother_and-Modes/tree/master/ETC/patches/S%20-%20A1_AFlower_Sauce)  An L-system implementation producing a Flower/Leaf. 
* [S - A1_APopulation_Chaos](https://github.com/sylatupa/Video_Synth-ETC_Mother_and-Modes/tree/master/ETC/patches/S%20-%20A1_APopulation_Chaos)
*[S - A1_Brownian_Sauce](https://github.com/sylatupa/Video_Synth-ETC_Mother_and-Modes/tree/master/ETC/patches/S%20-%20A1_Brownian_Sauce)

Code attributions found in each file. Also, here are those sources:
http://www.mediafire.com/file/5rteoppprwqcb72/flowersystem.py
https://www.pygame.org/project/1755/3062
Chaos fractal like here:  https://www.pygame.org/project/1754

![lsystem]

## parallel_projects

The Digital_Thing is built in the context of a Digital Culture, Arts Media and Engineering, Master of Arts program and some of the following project examples are with interactive art and media. 
* [Digital_Culture_Server](https://github.com/sylatupa/Digital_Culture_Server)
** A collection of Node-Red Flows and Python Scripts. This runs on a Raspberry Pi and is connected to WiFi.
** The Digital_Thing takes sensor data and sends it over an MQTT Network. Node Red recieves this data and sends it the ETC Video Synthesizer and the Digital_Culture_Sound_Client, over OSC.  
* [Digital_Culture_Sound_Client](https://github.com/sylatupa/Digital-Culture-Sound-Client)
** A sound synthesizer written in Pure Data. This runs on a Raspberry Pi and is connected to Wifi and controlled by Node-Red and This_Thing.
* [Video_Synth-ETC_Mother_and-Modes](https://github.com/sylatupa/Video_Synth-ETC_Mother_and-Modes)
** written by Critter and Guitari for the ETC. This is installed on a Raspberry Pi that is connected to WiFi and controlled by Node-Red and This_Thing.

![pop_chaos2]

## See all the videos here:
https://www.youtube.com/watch?v=zzlslcG2fdA&list=PLcqKf5XU9uVOfuwFNbiraGHOt9Q5JuXdf

## An Arizona State University Herberger, Institute for the Design and the Arts, Digital Culture Masters Final Project, 2019.
[pop_chaos]: ./Images/population_image3.png
[pop_chaos2]: ./Images/population_image1.png
[lsystem]: ./Images/l-system.png

