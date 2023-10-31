from gtts import gTTS
from playsound import playsound

tts = gTTS(text="Aur kaise ho papa ji",lang="en", slow=False)
tts.save("audio.mp3")
playsound("audio.mp3")