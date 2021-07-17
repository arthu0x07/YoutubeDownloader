from moviepy.editor import *;
import os;

mp4_file = r"C:\Users\arthu\Desktop\Projeto Pytube\YoutubeDownloader\YoutubeDownloader\Musics\Python Convert Mp4 to Mp3 File Using MoviePy Library Full Project For Beginners.mp4"
mp3_file = r"C:\Users\arthu\Desktop\Projeto Pytube\YoutubeDownloader\YoutubeDownloader\Musics\Python Convert Mp4 to Mp3 File Using MoviePy Library Full Project For Beginners.mp4"
           r"C:\Users\arthu\Desktop\Projeto Pytube\YoutubeDownloader\YoutubeDownloader\Python Convert Mp4 to Mp3 File Using MoviePy Library Full Project For Beginners.mp4"


VideoClip = VideoFileClip(mp4_file)
AudioClip = VideoClip.audio;
AudioClip.write_audiofile(mp3_file)
AudioClip.close;
VideoClip.close;

### Funcionou por conta do caminho alternativo;
### um path mp3 e outro mp4 > objetivo, conseguir esses paths,

#palavra = r"C:\Users\arthu\Desktop\Projeto Pytube\YoutubeDownloader\YoutubeDownloader\Musics\Primeiro vídeo - Timelapse NetherHub 1.mp4"
#palavra = palavra.replace(".mp4", ".mp3");

print(palavra);