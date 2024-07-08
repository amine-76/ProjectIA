import speech_recognition as sr
import openai
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
 r = sr.Recognizer()
 with sr.Microphone() as source:
     print("Listening...")
     audio = r.listen(source)
     try:
         text = r.recognize_google_cloud(audio, language='fr-FR')
         print(f"You said: {text}")
         return text
     except sr.UnknownValueError:
         print("Sorry we could not understand audio")
         return "None"
     except sr.RequestError as e:
         print("Could not request results from Google Speech")
         return "None"



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True :
        print("Welcome to the Amine Project ! \n")
        print("It's your turn !")
        text = listen()
        print("You said: " + text)