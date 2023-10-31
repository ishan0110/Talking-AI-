import os
import openai
import speech_recognition as sr
import gtts
from playsound import playsound

from api_secret import API_KEY

openai.api_key = API_KEY

r = sr.Recognizer()
mic = sr.Microphone(device_index=0)

conversation = ""
username = "Ishan"

while True:
    with mic as source:
        print("Recording....")
        r.adjust_for_ambient_noise(source, duration=0.3)
        audio = r.listen(source)
    print("Recording completed..")
    
    try:
        user_input = r.recognize_google(audio,language="en")
    except Exception as e:
        print(e)
        continue
    prompt = username+": "+user_input+"\nBot: "
    conversation += prompt
    print(prompt)
    
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = conversation,
        temperature = 0.5,
        max_tokens = 4000,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0
    )
    
    response_str = response["choices"][0]["text"].strip()
    
    print(response_str)
    
    tts = gtts.gTTS(str(response_str), lang="en")
    tts.save("output.mp3")
    playsound("output.mp3", block=True)
    os.remove("output.mp3")