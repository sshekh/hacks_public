[Removed some hacks :p ]
#brightness
use: brightness $number
0<$number<100 set brightness to $number %

#brightness-down
use: brightness-down
decrements brightness by 4%

#brightness-up
use: brightness-up
increments brightness by 4%

#checkmail
use: checkmail
gives my unread gmails

#cim
use: cim file.cpp
creates file.cpp with predefine template, compiles to file.cpp.out

#clean
use: clean
removes unwanted files, currently *.out

#delsong
use: delsong
adds entry of currently playing song in /media/downloads/songs_to_be_deleted, which can be deleted in windows

#list
use: list
loads windows, if not already loaded, list all playlists, lists all songs from selected playlist and play the selected

#mess\ menu
use: mess\ menu
gives today's mess menu, taking input from mess\ menu\ from\ doc
and time remaing (in hours) to reach home! :P

#myplay
use: myplay <song_name>
plays the song along with beat pattern as the terminal title

#mystop
use: mystop
stops the myplay command, killing all child processes

#news
use: news OR news {query}
displays top stories or news about {query}

#resume
use: resume
compile my resume and send it to my homepage

#rim
use rim: file.cpp
same as cim, except opertaes in pre-existing file

#startup.sh
use: sudo startup.sh
my startup script, for powerconservation

#togglevim
use: togglevim
toggles between customized vim and bare vim

#weather
use: weather (or alt+w)
gives current weather in bangalore

#windows_mount
use: windows_mount
mounts windows to /media/windows and downloads to /media/downloads
