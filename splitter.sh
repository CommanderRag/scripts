echo "Enter url:"

read URL 

title=$(youtube-dl -o '%(title)s.%(ext)s' --skip-download --get-title --no-warnings $URL | sed 2d)

echo "Downloading from $URL with title $title"

echo -e "\n"

echo "Downloading video file..."

echo -e "\n"

youtube-dl -o '%(title)s.%(ext)s' -f 'bestvideo[height<=720]'  $URL

echo -e "\n"

echo "Downloading audio file..."

echo -e "\n"

audio=$(youtube-dl -o '%(title)s.%(ext)s' -f 140 --skip-download --get-title --no-warnings $URL |sed 2d)

youtube-dl -o '%(title)s.%(ext)s' -f 140 $URL

a="${title}.mp4"
c="${audio}.m4a"

echo -e "\n"

ffmpeg -i "${a}" -i "${c}" -c:v copy -c:a aac "storage/shared/${a}"

echo -e "\n"

rm "${a}"
rm "${c}"

echo 'Done...'

exit
