import sys
import os

dir_path = os.path.dirname(os.path.realpath(sys.argv[1]))

for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith(f'.m4a'):
            os.system('ffmpeg -i ' + 'C:\\Users\\MH\\Documents\\Coding\\MP3Ripper\\P3R\\' + file + ' -filter:a "atempo=1.5" -vn "nc_' + file)
            os.remove('C:\\Users\\MH\\Documents\\Coding\\MP3Ripper\\P3R\\' + file)