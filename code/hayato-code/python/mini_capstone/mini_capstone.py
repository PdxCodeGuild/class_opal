'''
***PLEASE USE THIS TOOL WITH RESPONSIBILITY, 
AND I AM NOT RESPONSIBLE FOR ANY MUSIC DOWNLOADED 
WITH THE INTENT TO SELL, DISTRIBUTE, OR UTILIZE IT 
IN A FASHION THAT COULD INFRINGE ON COPYRIGHT LAWS.*** 

'''
# Librosa for getting the beats per minute, Pytube to download videos from youtube, moviepy to edit the video from pytube to MP3 format. 
import librosa
from pytube import YouTube, Stream
from moviepy.editor import *

def music_downloader():
    # url input from user
    yt = YouTube(
        str(input("Enter the URL of the video you want to download: \n>> ")))
    
    # extract the highest quality video from YouTube
    video = yt.streams.get_highest_resolution()
    
    # download the file to the current directory
    video.download()
    
    # result of success
    print(yt.title + " has been successfully downloaded.")
    
    #taking the original youtube title to replace the periods and commas to allow the files to be found later. 
    youtube_title = yt.title.replace('.', '').replace(',', '')
    
    music_convertor(youtube_title)

    return youtube_title


def music_convertor(proper_yt_title):
    music_file = proper_yt_title

    #Calling the file in directory as mp4 format that originated from pytube
    mp4_file = f"{music_file}.mp4"

    #Rewriting the file in directory as mp3 format for Librosa to run the beats per minute.
    mp3_file = f"{music_file} - audio.mp3"

    #Grabbing the clip from pytube to allow moviepy to extract specified information
    videoclip = VideoFileClip(mp4_file)

    #Grabbing strictly the audio from the clip using moviepy
    audioclip = videoclip.audio

    #Reformating the clip from mp4 to mp3 
    audioclip.write_audiofile(mp3_file)

    #closes the internal reader
    audioclip.close()

    #closes the internal reader
    videoclip.close()

    bpm_analysis(music_file)

def bpm_analysis(music_file):

    # 1. Get the file path 
    filename = f"{music_file} - audio.mp3"

    # 2. Load the audio as a waveform `y`
    #    Store the sampling rate as `sr`
    y, sr = librosa.load(filename)

    # 3. Run the default beat tracker
    tempo, beat = librosa.beat.beat_track(y=y, sr=sr)

    print(f'Estimated tempo: {round(tempo, 2)} beats per minute')

while True: 
    user_question = input(f"Hi! I'm going to figure out the beats per minute for the song of your choice on YouTube press enter to continue. If you would like to exit press q ").lower()
    if user_question == 'q':
        break
    elif user_question != 'q':
        music_downloader() 
        break

    
    

