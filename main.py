#importing modules
import os
import time
from datetime import datetime
import random
import speech_recognition as sr
import pyttsx3
import numpy as np
import requests
import json
from bs4 import BeautifulSoup
import pyperclip
import string

#importing modules for web search
from googlesearch import search

#importing wikipedia module
import wikipedia

#note making modules
import subprocess

#internet speed modules
import speedtest as sp

#GUI module 
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk

#import game files
import guessme
import Numcrick
import RockPaperScissor
import whatthecolor
import Jumbbled

#import jokes module
import pyjokes

#importing module for facts
import randfacts

#importing module for articles
#imporing modules for movies
import webbrowser as wb

#making the assistant speak
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 130) 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#taking voice input from user
def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""

		try:
			said = r.recognize_google(audio)
			print(said)
		except Exception as e:
			speak("Can you say that again please")
	return said


#wish function
def wish():
	hour = int(datetime.now().hour)
	if hour>=0 and hour<=12:
		speak("Good Moring")
	elif hour>=12 and hour<=15:
		speak("Good Afternoon")
	else:
		speak("Good Evening")
	speak("i am Random, How can i help you")

name_list = np.array(["what is your name","who are you"])

#note
def note(text):
	date = datetime.now()
	file_name = str(date).replace(":","-")+"-note.txt"
	with open(file_name,"w") as f:
		f.write(text)
	subprocess.Popen(["notepad.exe",file_name])
note_list = np.array(['make a note','write this down','note','remember this'])

#weather
def weather(city):
	search = f"temperature in {city}"
	url = f"https://www.google.com/search?q={search}"
	r = requests.get(url)
	w_data = BeautifulSoup(r.text,"html.parser")
	temp = w_data.find("div",class_ = "BNeawe").text
	speak(f"current {search} is {temp}")
#news function
def news():
	API_KEY = "XXXXXXXXXXXXXXXXXXXX"
	news_url = f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={API_KEY}"
	news = requests.get(news_url).json()
	n_article = news["articles"]

	news_headlines = []
	for arti in n_article:
		news_headlines.append(arti['title'])

	for i in range(5):
		speak(f'headline {i+1} is {news_headlines[i]}')
		
#internet speed function
def internet_speed():
	st = sp.Speedtest()
	dl = st.download()
	up = st.upload()
	speak(f"the upload speed is {up // 8000000} MB per second and download speed is {dl // 8000000} MB per second")

#password genration
def passgen():
	letters = string.ascii_letters
	num = string.digits
	spchar = string.punctuation
	plist = []
	plist.extend(list(letters)+list(num)+list(spchar))
	random.shuffle(plist)
	Password = "".join(plist[0:8])
	pyperclip.copy(Password)
password_list = np.array(["generate a password","can you generate a Password for me","password"])

def main():
	wish()
	while True:
			print("Listing...")
			command = get_audio().lower()

			if command in name_list:
				speak("My name is random")
			#wikipedia
			elif "wikipedia" in command:
				speak('Searching Wikipedia...')
				command = command.replace("wikipedia", "")
				results = wikipedia.summary(command, sentences=2)
				speak("According to Wikipedia")
				speak(results)


			#google search
			elif "search" in command:
				speak("What you want me to search")
				s_word = get_audio().lower()
				for i in search(s_word,tld = "co.in",num = 1,start = 1 ,stop = 1):
					speak("Here, this is what i found on web")
					wb.open(f"{i}")


			#notemaking feature	
			elif command in note_list:
				speak("what you want me to note down")
				note_text = get_audio()
				note(note_text)
				speak("I Noted that")
				
			#weather feature 
			elif "weather" in command:
				speak("In which city")
				i_city = get_audio()
				weather(i_city)
				
			#games feature
			elif "game" in command:
				speak(' Opening a random game for you to play')
				ch = random.randint(1,5)
				if ch == 1:
					guessme.main()
				elif ch == 2:
					Numcrick.main()
				elif ch == 3:
					RockPaperScissor.main()
				elif ch == 4:
					whatthecolor.main()
				elif ch == 5:
					Jumbbled.main()
			#news feature
			elif "news" in command:
				speak('here are few top-headlines')
				news()

			#password genration
			elif command in password_list:
				speak("ok sure, just a moment")
				passgen()
				speak("your password is copied to clipboard")

			#internet speed feature
			elif "internet speed" in command:
				speak("sure just a moment")
				internet_speed()
			#music
			elif "music" in command:
				speak('ok sure')
				music_dir = 'D:\\songs'
				songs = os.listdir(music_dir)
				i = random.randint(1,3)
				os.startfile(os.path.join(music_dir, songs[i]))

			#movies
			elif "movie" in command:
				wb.open('https://www.netflix.com/browse/my-list')
				speak(' Playing a movie for you')

			#article
			elif "article" in command:
				speak(' Opening a wikipedia Article for you to read')
				wb.open('https://en.wikipedia.org/wiki/Special:Random')

			#jokes
			elif "joke" in command:
				joke = pyjokes.get_joke(language = 'en',category = "neutral")
				speak(f"sure {joke}")

			#fact
			elif "fact" in command:
				fact = fact = randfacts.getFact()
				speak(f'sure {fact}')

			#app open
			elif "open vs code" in command:
				os.startfile("C:\\Users\\dhanu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
				speak("Opening Visual Studio code")

			elif "open notepad" in command:
				os.startfile("%windir%\\system32\\notepad.exe")
				speak("Opening notepad")

			elif 'open youtube' in command:
				wb.open("https://youtube.com")
				speak("Opening youtube")

			elif 'open google' in command:
				wb.open("https://google.com")
				speak("Opening google")

			elif 'open stackoverflow' in command:
				wb.open("https://stackoverflow.com")
				speak("Opening stackoverflow") 

			elif 'open github' in command:
				wb.open('https://github.com/')
				speak("Opening github")

			#time
			elif "time" in command:
				strTime = datetime.now().strftime("%H:%M:%S")
				speak(f"Sir, the time is {strTime}")


			#quit
			elif "quit" in command:
				speak('Bye, I am quitting')
				break

			else:
				speak("I can't do that for you sorry")
#GUI
root = Tk()
root.title("Random")
path = "guiimg.jpeg"
img = ImageTk.PhotoImage(Image.open(path))
label = tk.Label(root, image = img)
label.pack()
Start_Button = Button(root,text = "Start",command = main)
Start_Button.pack()
Quit_Button = Button(root,text = "Quit",command = root.destroy)
Quit_Button.pack()
root.mainloop()
