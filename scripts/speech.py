import speech_recognition as sr
# Create a recognizer object
r = sr.Recognizer()
# Record audio from the microphone
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
# Convert the audio to text
try:
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Sorry, I could not understand what you said")
except sr.RequestError as e:
    print("Error; {0}".format(e))