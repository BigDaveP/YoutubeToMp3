
# Editer le fichier JSON pour ajouter des liens de téléchargement

from pytube import YouTube
import os
from moviepy.editor import *
import json
import shutil

def Download():
    arr = json.loads(open("Link.json", "r").read())
    for link in arr["link"]:
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_lowest_resolution()
        try:
            youtubeObject.download()
        except:
            print("An error has occurred")
        print("Download is completed successfully")

def ConvertToMP3():
    for file in os.listdir():
        if file.endswith(".mp4"):
            clip = VideoFileClip(file)
            clip.audio.write_audiofile(f"{file[:-4]}.mp3")
            clip.close()
            if not os.path.exists(f"mp3/{file[:-4]}.mp3"):
                os.rename(f"{file[:-4]}.mp3", f"mp3/{file[:-4]}.mp3")
                os.remove(file)

while True:
    choice = input("Télécharger (t) ou Convertir les fichier (c) : ")
    if choice == "t":
        Download()
    elif choice == "c":
        ConvertToMP3()

