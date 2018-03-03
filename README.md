
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install alsa-utils
sudo modprobe snd_bcm2835
sudo apt-get install mplayer

sudo pip install gTTS
```

Add the following line to /etc/mplayer/mplayer.conf:
```
nolirc=yes
```

Since your speakers are probably connected to the headphones jack socket you may want to force the output to it:
```
amixer cset numid=3 1
```

Test that the audio output work
```
sudo aplay /usr/share/sounds/alsa/Front_Center.wav
```
