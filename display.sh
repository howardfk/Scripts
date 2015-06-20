#!/bin/bash
#Practice making  display manipulations
savedir=/Users/howard/Documents/Geeklets/display_temp.txt

rezold=$(<$savedir)
rez=$(system_profiler SPDisplaysDataType | grep "Resolution*" | awk '{print $2, $3, $4}')
#rez=$(xdpyinfo | grep dimensions | awk '{print $2}' | awk -Fx '{print $1, $2}')

echo "$rez" > "$savedir"

if [ "$rezold" != "$rez" ]; then
    if [ "$rez" == "2560 x 1600" ]; then
        osascript /Users/howard/Documents/Geeklets/smallscreen.scpt 
    else
        osascript $HOME/Documents/Geeklets/largescreen.scpt
    fi
fi
