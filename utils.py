import wikipedia
from AppOpener import open as app_open
import datetime
import webbrowser
from voice_engine import speak


def search_wikipedia(query):
    speak("Searching Wikipedia....")
    query = query.replace('wikipedia', "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    speak(results)


def open_application(query):
    try:
        app_name = query.replace('open application', '').strip()
        app_open(app_name, match_closest=True)
        speak(f"Opening {app_name}")
    except Exception as E:
        print(E)
        speak("Sorry, we couldn't open that application right now. Please try again.")


def get_time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {strTime}")


def web_search(query):
    query = query.replace("search", "").replace("play", "").strip()
    webbrowser.open(query)
    speak(f"Searching for {query}")
