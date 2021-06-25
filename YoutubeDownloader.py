from os import link
from pytube import YouTube;
import time;


linksArray = [];


def Apresentacao():
    Saltos(100);

    print("Youtube Downloader - Kraddie");
    Saltos(1);

    print(" >> Fazer Download de músicas                         : (1) ");
    print(" >> Fazer Download de vídeos                          : (2) ");
    print(" >> Checar Informações sobre política de distribuição : (3) ");

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
    rangeReached = False;

    while(rangeReached == False):

        for i in range(0, len(linksArray)):
            yt = YouTube(linksArray[i]);
            stream = yt.streams.filter(only_audio=True).first();
            stream.download(max_retries=3);
    


# >> Área do programa...

Apresentacao()


