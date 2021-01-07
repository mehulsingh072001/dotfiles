#! /bin/bash 
picom &
urxvtd -q -o -f &
xset led named "Scroll Lock"
feh --bg-scale ~/.config/qtile/wallpapers/empty.jpg
nm-applet &
blueman-applet &
xinput set-prop "ELAN1300:00 04F3:3057 Touchpad" "libinput Tapping Enabled" 1 &
mpd &
redshift-gtk -l 27.2046:77.4977 &
xfce4-power-manager
barrier &
emacs --daemon
