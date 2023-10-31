import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone(device_index=0) as source:
    print("Talk")
    audio = r.listen(source)
    
try:
    print(r.recognize_google(audio, language="en"))
except sr.UnknownValueError:
    print("Unknown voice")
except sr.RequestError as e:
    print("Not clear (0) ".format(e))
    
    