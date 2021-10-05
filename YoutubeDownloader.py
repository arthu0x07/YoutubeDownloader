import os;
from pytube import YouTube;
import time;
import re;
from moviepy.editor import *;


linksArray = [];
Paths = [];


def Apresentacao():
    Saltos(100);

    print("Youtube Downloader - Kraddie");
    Saltos(1);

    print(" >> Fazer Download de músicas                         : (1) ");

    choice = input()

    #vai enviar um parâmetro que vai diferenciar se é pra receber links e levar para o downloader de audios ou videos comparando o parâmetro.
    if(choice == '1'):
        ReceiveLinks('ad');

    
#    if(choice == '2'):
 #       MakeDownloadsVideos();

    
#    if(choice == '3'):
 #       Informations(); 

    else:
        Naoentendi();



def Naoentendi():
    Saltos(100);
    print("Não pude entender, digite novamente em 3 segundos...");
    time.sleep(1);
    print("Não pude entender, digite novamente em 2 segundos...");
    time.sleep(1);
    print("Não pude entender, digite novamente em 1 segundo...");
    time.sleep(1);

    Apresentacao();



def Saltos(saltos = ''):
    Paramint = 1;
    Paramfloat = 1.1;

    if(type(saltos) == type(Paramint) or type(saltos) == type(Paramfloat)):
        print("\n" * saltos);

    else:
        print("\n");


#Pega os links, guarda num array, e joga o array para a prox função sem formatar para a proxima função. Compara se o link é "F", para não adicionar no array.
def ReceiveLinks(comparate = None):
    actualLink = '';
    global linksArray;
    
    #Se o usuário digitar f ou F ele finaliza antes de colocar o input no array.
    while(actualLink != 'F' and actualLink != 'f'):
        print("Por favor, vá digitando seus links, caso não queira mais, insira a letra 'F'. ");
        actualLink = input();

        if(actualLink != 'f' and actualLink != "F"):
            linksArray.append(actualLink);
        
        actualLink = actualLink.upper();
        Saltos();

    Saltos(100);
    print("Seus links até agora são estes: ");
    for i in range(0, len(linksArray)):
        print("Link: " + linksArray[i] + " | " + YouTube(linksArray[i]).title);
    
    time.sleep(3);
    Saltos(); #Limpa o console.

    print("Vamos prosseguir...");
    time.sleep(1);

    if(comparate == 'ad'):
        MakeDownloadsAudios();


def MakeDownloadsAudios():
    global linksArray;

    for i in range(0, len(linksArray)):
        yt = YouTube(linksArray[i]);
        stream = yt.streams.filter(progressive=False).first();
        stream.download(output_path=str('musics/'), max_retries=3);

        time.sleep(5);

    Converting();



def Converting():
    Saltos()
    Range = False;

    print("Agora vamos converter...")

    pasta = './musics'
    
    for root, dirs, files in os.walk("./Musics", topdown=False):
        for name in files:
            diretorio = os.path.join(root, name)

            mp4_file = str(diretorio);
            #erro nesta linha, extensao errada (do arquivo e )
            caminhomp3 = re.sub(r'.3gpp|.mp4|.wav|.avi|.FLV|.MOV|.MKV|,', '.mp3', diretorio);
            mp3_file = str(caminhomp3);
            
            VideoClip = VideoFileClip(mp4_file)
            AudioClip = VideoClip.audio;
            AudioClip.write_audiofile(mp3_file)
            AudioClip.close;
            VideoClip.close;


Apresentacao();


#Fazer uma checagem pra ver se o arquivo possue a extenção .mp3 (para ignorar tal arquivo)...

#Fazer uma forma de mostrar quais downloads estão sendo executados...

#Reescrever a leitura de diretorios antes de commitar...


