import speech_recognition as sr
import pyttsx3

def speak(text):
    
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "_main_":
    speak("Hello, I am your voice assistant. How can I help you?")
    while True:
        text = get_audio()
        if text.lower() == "exit":
            speak("Goodbye!")
            break
        
        if "play music" in text.lower():
            speak("Playing music.")
            
        elif "set alarm" in text.lower():
            speak("Setting alarm.")
            
        else:
            speak("I'm still learning. Try asking me something else.")