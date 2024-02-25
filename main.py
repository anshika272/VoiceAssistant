import speech_recognition as sr # recognise speech
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import ctime # get time details
import webbrowser # open browser
import time
import spotipy
import pyttsx3
import pywhatkit
import g2
import tumor


username = 'kj5nvr9kb8j2xyo4fuazffkld'
clientID = '1993152982284d929a090c62af06c113'
clientSecret = '9e1d4b5b12cb4c1eb39c0c2414584184'
redirectURI = 'http://google.com/'



engine = pyttsx3.init()
def alex_says(string):
    engine.say(string)
    engine.runAndWait()



r = sr.Recognizer() # initialise a recogniser
print('Speak...')


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True


# listen for audio and convert it to text:
def record_audio(ask=False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            print(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio) 
            #print(voice_data) # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            print('I did not get that')
        except sr.RequestError:
            print('Sorry, the service is down') # error: recognizer is not connected
        print(voice_data) # print what user said
        return voice_data

# get string and make a audio file to be played
def whatsapp_sendmsg(msg,hour,min):
    pywhatkit.sendwhatmsg("+917828770482",msg,hour,min)


def play_spotify(song_name):
    oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)
    token_dict = oauth_object.get_access_token()
    token = token_dict['access_token']
    spotifyObject = spotipy.Spotify(auth=token)
    user = spotifyObject.current_user()

    alex_says("Welcome, "+ user['display_name'])
         # Get the Song Name.
    searchQuery = song_name
        # Search for the Song.
    searchResults = spotifyObject.search(searchQuery,1,0,"track")
        # Get required data from JSON response.
    tracks_dict = searchResults['tracks']
    tracks_items = tracks_dict['items']
    song = tracks_items[0]['external_urls']['spotify']
        # Open the Song in Web Browser
    webbrowser.open(song)
    alex_says('Song has opened in your browser.')
        

def respond(voice_data):
    # 1: greeting
    if there_exists(['hey','hi','hello']):
        greetings = ["hey, how can I help you ", "hey, what's up? ", "I'm listening ", "how can I help you? ", "hello "]
        greet = greetings[random.randint(0,len(greetings)-1)]
        alex_says(greet)
        print(greet)

    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        alex_says("my name is Alex")
        print("my name is Alex")



    # 3: greeting
    if there_exists(["how are you","how are you doing"]):
        alex_says("I'm very well, thanks for asking ")
        print("I'm very well, thanks for asking ")


    # 4: time
    if there_exists(["what's the time","tell me the time","what time is it","time"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + ':' + minutes
        alex_says('The time is '+time )
        print('The time is '+time )


    # 5: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        alex_says('Here is what I found for '+search_term+' on google\n')
        print('Here is what I found for '+search_term+' on google\n')


    # 6: search youtube
    if there_exists(["open YouTube"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.youtube.com/results?search_query="+search_term
        webbrowser.get().open(url)
        alex_says('Here is what I found for '+search_term+' on youtube\n')
        print('Here is what I found for '+search_term+' on youtube\n')


    if there_exists(["find location"]):
        search_term = voice_data.split("location")[-1]
        url = "https://google.nl/maps/place/" + search_term +'/&amp;'
        webbrowser.get().open(url)
        alex_says('Here is what I found for '+ search_term +' on google maps\n')
        print('Here is what I found for '+ search_term +' on google maps\n')

    
    if there_exists(["open WhatsApp"]):
        url ="https://web.whatsapp.com/" 
        webbrowser.get().open(url)
        alex_says("opening whatsapp")
    
    if there_exists(["Spotify","Open Spotify"]):
        search_term = voice_data.split("play")[-1]
        # play fight song on spotify
        play_spotify(search_term)
        alex_says("playing" + search_term + "on spotify\n")
        print("playing" + search_term + "on spotify\n")

    if there_exists(["open Google meet","Google meet"]):
        alex_says("enter the meeting code")
        meeting_code = input("enter the meeting code:")
        url = "https://meet.google.com/" + meeting_code
        alex_says("Enter email and password")
        mail_address = input("Enter email address:")
        password = input('Enter password:') 
        alex_says("opening gmeet")
        g2.gmeet(mail_address,password,url)

    if there_exists(["send message"]):
        alex_says("Enter the msg")
        msg = input("Enter the msg:")
        alex_says("Enter the hour at which you want to send the msg in 24 hour format")
        hourtime = int(input("Enter the hour at which you want to send the msg in 24 hour format:"))
        alex_says("Enter the min at which you want to send msg")
        min = int(input("Enter the min at which you want to send msg:"))
        alex_says("Sending the msg to mummy")
        whatsapp_sendmsg(msg,hourtime,min)

    if there_exists(["open project"]):
        search_term = voice_data.split("project")[-1]
        tumor.tumor()


    if there_exists(["exit", "quit", "goodbye"]):
        alex_says("going offline\n")
        print("going offline\n")
        exit()


time.sleep(1)

while(1):
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond
