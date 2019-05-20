import speech_recognition as sr
import pyaudio
import webbrowser

## Voice_Recognition
r = sr.Recognizer()
with sr.Microphone() as source :    
    print('Speak Now:')
    audio = r.listen(source)

    try:
        print('Listening')
        text = r.recognize_google(audio)
        print('You said: {}'.format(text))
        txt = text;
        if txt.split()[0] == 'Google'  :
            new = 2 
            url = "http://google.com/?#q=";
            webbrowser.open(url+text,new = new);
        else:
            print('Try adding google in Start');
    except:
        print('Sorry could not understand')
