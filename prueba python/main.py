import pyttsx3 as voice
import pruebaspoti as pspoti
import pandas as pd

engine = voice.init()


""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate                    #printing current voice rate
engine.setProperty('rate', 150.0)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)             #printing current volume level
engine.setProperty(volume,100.0)    # setting up volume level  between 0 and 1


"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female



def text_to_speech(text):
    #engine connects us to hardware in this case 
    eng= voice.init()
    #Engine created 
    eng.say(text)
    #Runs for small duration of time ohterwise we may not be able to hear
    eng.runAndWait()
    engine.stop()
    engine.save_to_file(text, 'test.mp3')
    engine.runAndWait()
    engine.stop()

artista = pspoti.Artista().obtener_id_artista()
album = pspoti.Album(artista)
cancion = pspoti.Cancion(artista)

print(cancion.top_canciones())

with open("Lista_Album.txt","w") as archivo2:
        for linea in album.buscar_albums_artista():
            archivo2.write(linea+"\n")

with open("Lista_Album.txt","r") as archivo:
    for linea in archivo:
        print(linea)
        text_to_speech(linea)


with open("Lista_Cancion.txt","w") as archivo3:
    for linea in cancion.top_canciones():
        archivo3.write(linea+"\n")
        
with open("Lista_Cancion.txt","r") as archivo4:
    for linea in archivo4:
        print(linea)
        text_to_speech(linea)
        text_to_speech(linea)
