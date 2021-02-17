echo "Enter url:"

read URL 

title=$(youtube-dl --get-filename  -f '[ext=mp4]' --no-warnings $URL)

echo "Downloading from $URL with title $title"

echo -e "\n"

echo "Downloading video file..."

echo -e "\n"

youtube-dl  -f '[ext=mp4]'  $URL

echo -e "\n"

echo "Downloading audio file..."

echo -e "\n"

audio=$(youtube-dl --get-filename  -f 'bestaudio[ext=m4a]' --no-warnings $URL)

youtube-dl -f 'bestaudio[ext=m4a]' $URL

a="${title}"
c="${audio}"

echo -e "\n"

ffmpeg -i "${a}" -i "${c}" -c:v copy -c:a aac "storage/shared/Downloaded/${a}"

echo -e "\n"

rm "${a}"
rm "${c}"

echo 'Done...'

exit
