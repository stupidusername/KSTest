# KSTest

This app was made to reproduce an audio error that was found while using Kivy
and Raspbian Stretch Lite.

## Error description

After playing an audio file using the class `SoundLoader` through the audio
jack you can hear a hiss that never stops (it keeps going after the sound
playback is completed). After that, if `aplay` is used to play another sound,
the sound playback is broken in ways that are hard to describe in words.

## Context

* OS: Raspbian Stretch Lite after PWM audio driver change (see [Analogue audio redux](https://www.raspberrypi.org/forums/viewtopic.php?f=29&t=195178)).
* Kivy version: v1.11.0.dev0.
* Kivy audio implementation: gstplayer.
* Audio output: 3.5mm audio jack.

## Steps to reproduce

* Install Raspbian Stretch Lite. [Download page](http://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2018-06-29/).
* Install Kivy >= 1.11.0 (only tested in v1.11.0.dev0). [Instructions](https://kivy.org/docs/installation/installation-rpi.html).
* Connect a set of speakers/headphones to the audio jack.
* Clone this repo.
* Run the app `$ python main.py`.
* Press play. After the file is done playing you should hear a hiss.
* Exit the app (by pressing `Esc`).
* Test sound output with `$ aplay /usr/share/sounds/alsa/Front_Center.wav`. The
sound should be all broken.

## Temporary fix

* Change the PWM mode:
```
$ sudo nano /boot/config.txt
```
Add this at the end of the file.
```
audio_pwm_mode=1
```
* Reboot.
```
$ sudo reboot
```
