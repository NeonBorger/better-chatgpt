from subprocess import call
import os
from gtts import gTTS
while True:
  text=input("Enter text>")
  language = 'en'
  gttsFile = gTTS(text=text, lang=language, slow=False)
  gttsFile.save("gtts.mp3")
  os.system("mpg321 -q gtts.mp3")

