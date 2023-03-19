import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

# Initialize speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to speak a given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to recognize speech input
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except:
        print("Sorry, I could not understand.")
        return ""

# Define the main function for the voice assistant
def main():
    # Greet the user
    speak("Hello! How can I help you today?")

    while True:
        # Get the user's speech input
        text = recognize_speech().lower()

        # Perform actions based on the input
        if "what time is it" in text:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            speak("The time is " + now)
        elif "search wikipedia for" in text:
            query = text.replace("search wikipedia for", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia, " + results)
        elif "open website" in text:
            url = "https://www.google.co.in"
            webbrowser.open(url)
            speak("Opening Google")
        elif "play kgf 2 kannada song" in text:
            url = "https://www.youtube.com/watch?v=Vl-VFHtkE6w"
            webbrowser.open(url)
        elif "exit" in text:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I did not understand. Please try again.")

if __name__ == '__main__':
    main()