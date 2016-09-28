# ffmpeg -f alsa -i hw:1 -t 5 -y sound.wav
# echo "Transfiriendo"
# scp sound.mp3 MUSICBERRY:/home/pi > /dev/null
echo "Ejecutando"
# ssh MUSICBERRY "omxplayer -o local sound.mp3" > /dev/null
omxplayer -o local sound.mp3 > /dev/null
echo "Completado"
