import yt_dlp as youtube_dl
import sys
import os


dir_path = os.path.dirname(os.path.realpath(__file__))

def execute():
    if sys.argv[1] == '-ff':
        ydl_opts = {
            'format': 'bestaudio/best',
            'cachedir': False,
            'outtmpl': dir_path + f'/{sys.argv[2]}',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            video = sys.argv[3:]
            ydl.download(video)

        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith(f'{sys.argv[2]}.mp3'):
                    os.system('ffmpeg -i ' + file + ' -filter:a "atempo=1.5" -vn new_' + file)
                    os.remove(file)
    else:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': dir_path + f'/{sys.argv[1]}',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.cache.remove()
            video = sys.argv[2:]
            ydl.download(video)

if __name__=='__main__':
    execute()
