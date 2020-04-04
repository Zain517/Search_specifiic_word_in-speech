import speech_recognition as sr 
search=input('Enter the Word that you want to Search in speech: ')
#obtain Audio from the Microphone
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Speak into Microphone....")
    audio = r.listen(source)
try:
    iput=r.recognize_google(audio, language='en-US')
    print("Transcription: " + iput)
    print("you are looking for: " +search)
    x=iput.upper().find(search.upper())
    if x >= 0:
        print('YES....!!! Found')
    elif x == -1:
         print("Not found Require word")
    
except sr.UnknownValueError:
    print("Audio unintelligible")
except sr.RequestError as e:
    print("Can't obtain result; {0}".format(e))        
