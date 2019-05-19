import speech_recognition as sr
import pyaudio
import webbrowser

## Voice_Recognition
r = sr.Recognizer()
with sr.Microphone() as source :    
    print('Speak:')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('You said: {}'.format(text))
    except:
        print('Sorry could not understand')
        
## Opening URL
new = 2 
tabUrl = "http://google.com/?#q=";
webbrowser.open(tabUrl+text,new = new);ss