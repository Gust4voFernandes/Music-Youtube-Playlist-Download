import re
import os
from pytube import Playlist

YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
#DOWNLOAD_DIR = 'C:\\Users\\lima0\\Music\\DowloadMusicas\\MusicasLuciene'
print("----------------------------------------------------------------------------------------")
print("------------------ Dowload de Playlist do Youtube em MP3 ------------------")

print("Caminho padrão = C:Users/ima0/Music/DowloadMusicas/MusicasLuciene")
op = input("Deseja alterar? S/N: ")
if op == 'S' or op == 's':
    try:
        DOWNLOAD_DIR = input("Insira o caminho de dowload seperado por 'duas barras invertidas': ") #\\
    except Exception as e:
        print("Caminho de arquivo inválido! ERRO: {} ".format(e))
else:
    DOWNLOAD_DIR = 'C:\\Users\\lima0\\Music\\DowloadMusicas\\MusicasLuciene'

try:
    playlist = Playlist(input("Link da Playlist: "))
except Exception as e:
    print("Link inválido! ERRO: {} ".format(e))

try:
    # isso corrige a lista playlist.videos vazia
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
except Exception as e:
    print("Problema ao corrigir lista vazia! ERRO: ".format(e))

print("Número de Videos: ",len(playlist.video_urls))
n = len(playlist.video_urls)
for url in playlist.video_urls:
    print(url)

try:
    # baixando a faixa de áudio
    for i, video in enumerate(playlist.videos, start=1):

        print('Baixando {}/{}: {} url : {}'.format(i, n, video.title, video.watch_url))
        audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
        audioStream.download(output_path=DOWNLOAD_DIR)

    print(DOWNLOAD_DIR)
    print("Dowload Completo! :)")
except Exception as e:
    print("Encontramos problemas ao fazer o download, verifique sua conexão! ERRO: {} ".format(e))
print("----------------------------------------------------------------------------------------")
os.system("pause")